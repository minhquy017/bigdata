from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import ccxt
import pandas as pd
import io
import boto3
from botocore.client import Config

# Hàm thực thi chính: Cào data và đẩy lên MinIO
def crawl_realtime_job():
    print("Bắt đầu lấy dữ liệu phút mới nhất...")
    exchange = ccxt.bitstamp()
    
    # 1. Lấy 1000 nến mới nhất tính đến thời điểm hiện tại
    btc_ohlcv = exchange.fetch_ohlcv('BTC/USD', '1m', limit=1000)
    df_btc = pd.DataFrame(btc_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df_btc['timestamp'] = pd.to_datetime(df_btc['timestamp'], unit='ms')
    df_btc['timestamp'] = df_btc['timestamp'] + pd.Timedelta(hours=7)
    
    # 2. Kết nối MinIO nội bộ
    s3_client = boto3.client(
        's3',
        endpoint_url="http://minio:9000",
        aws_access_key_id="admin",
        aws_secret_access_key="password123",
        config=Config(signature_version='s3v4')
    )
    
    # 3. Cập nhật file trên MinIO
    csv_buffer = io.StringIO()
    df_btc.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket="crypto-raw-data", Key='bitcoin_1m.csv', Body=csv_buffer.getvalue())
    print(f"Hoàn thành cập nhật {len(df_btc)} dòng dữ liệu realtime!")

# Cấu hình kịch bản Airflow
default_args = {
    'owner': 'minhquy',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1), # Để ngày trong quá khứ để Airflow chạy ngay lập tức
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
    'crypto_1m_realtime_pipeline',
    default_args=default_args,
    schedule_interval='* * * * *', # Lệnh bài: Chạy mỗi phút (* * * * *)
    catchup=False,
    tags=['crypto', 'realtime'],
) as dag:

    # Khai báo công việc (Task)
    task_crawl = PythonOperator(
        task_id='crawl_and_push_minio',
        python_callable=crawl_realtime_job
    )