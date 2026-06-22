# SV2 — Quý (Data Engineering / Docker / MinIO)

## Nhiệm vụ

- Cài đặt Docker Desktop và cấu hình Docker Compose
- Khởi chạy 4 services: Jupyter/PySpark, MinIO, PostgreSQL, Airflow
- Thu thập dữ liệu Bitcoin theo phút và 15 altcoins daily từ Bitstamp (ccxt)
- Upload dữ liệu lên MinIO bucket `crypto-raw-data`
- Xây dựng Airflow DAG tự động crawl BTC 1m mỗi phút

## Cấu trúc thư mục

```
sv2/
├── DA2-APP-01/
│   ├── compose.yaml              # Docker Compose 4 services
│   ├── README.md                 # Hướng dẫn setup hệ thống
│   └── Container_complete.png   # Ảnh container chạy thành công
├── DA2-DATA-01/
│   ├── dataset_description.txt  # Mô tả nguồn dữ liệu
│   ├── bitcoin_1m.csv           # BTC/USD 1 phút (1000 dòng)
│   └── altcoins_500d.csv        # 15 altcoins daily (500 ngày)
├── DA2-DATA-02/
│   ├── Airflow.png              # Ảnh Airflow DAG chạy thành công
│   └── MinIO.png                # Ảnh bucket MinIO
├── crawl_Data.ipynb             # Notebook crawl dữ liệu + upload MinIO
└── data/                        # Raw data (CSV)
    ├── bitcoin.csv
    └── altcoins.csv
```

## Issues

| Issue | Mô tả | Trạng thái |
|-------|-------|-----------|
| DA2-APP-01 | Thiết lập Docker, MinIO, Jupyter/PySpark và Airflow | ✅ 100% |
| DA2-DATA-01 | Thu thập dữ liệu Bitcoin và các đồng crypto | ✅ 100% |
| DA2-DATA-02 | Upload dữ liệu crypto vào MinIO và tự động hóa | ✅ 100% |

## Nguồn dữ liệu

- **Sàn giao dịch:** Bitstamp (qua thư viện `ccxt`)
- **Bitcoin:** 1000 nến 1 phút — BTC/USD
- **Altcoins:** 15 đồng × 500 ngày — ETH, XRP, LTC, LINK, UNI, MATIC, SOL, ADA, DOT, AVAX, DOGE, SHIB, BCH, ALGO, AAVE

## Airflow DAG

DAG `crypto_1m_realtime_pipeline` chạy mỗi phút:
1. Crawl 1000 nến BTC/USD mới nhất từ Bitstamp
2. Làm sạch dữ liệu (ép kiểu, loại bỏ rác)
3. Đẩy lên MinIO bucket `crypto-raw-data/bitcoin_1m.csv`
