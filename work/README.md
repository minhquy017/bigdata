# Đồ Án 2: Pipeline Dữ liệu Giao dịch Tiền điện tử (Crypto) và Bot RL

## Thông tin nhóm

| SV | Thành viên | Vai trò |
|----|------------|---------|
| SV1 | Dân | Team Leader / Requirement / Báo cáo |
| SV2 | Quý | Data Engineering / Docker / MinIO |
| SV3 | Hiếu | ETL / PySpark / Feature Engineering |
| SV4 | Khánh | Machine Learning / SVD / t-SNE |
| SV5 | Chương | Reinforcement Learning / DQN Bot |

## Kiến trúc hệ thống

```
Crypto API (Bitstamp)
        ↓
   Airflow DAG  (crawl mỗi phút)
        ↓
   MinIO bucket  (crypto-raw-data)
        ↓
   PySpark ETL  (làm sạch + indicators)
        ↓
   Parquet  (feature table + label)
        ↓
   ML Models  (Random Forest / Gradient Boosting)
        ↓
   SVD + t-SNE  (giảm chiều + visualization)
        ↓
   DQN Bot  (portfolio allocation)
```

## Cấu trúc thư mục

```
work/
├── sv1/          # Requirement, Project Plan, Phân công
├── sv2/          # Docker, MinIO, Dataset Crypto
├── sv3/          # ETL, Feature Engineering, Parquet
├── sv4/          # ML Buy/Sell, SVD, t-SNE
└── weekly_reports/
```

## Khởi chạy hệ thống

```bash
# Từ thư mục bigdata/
docker compose up -d

# Kiểm tra container
docker ps
```

| Service | URL | Tài khoản |
|---------|-----|-----------|
| Jupyter/PySpark | http://localhost:8888 | `docker logs pyspark-jupyter` |
| MinIO | http://localhost:9001 | admin / password123 |
| Airflow | http://localhost:8080 | `docker exec -it airflow_scheduler cat standalone_admin_password.txt` |
| PostgreSQL | localhost:5432 | admin / admin |

## Tech Stack

| Thành phần | Công nghệ |
|------------|-----------|
| Containerization | Docker Desktop |
| Object Storage | MinIO |
| Big Data Processing | PySpark |
| Notebook | Jupyter |
| Workflow | Apache Airflow |
| Data Format | Parquet |
| Machine Learning | Scikit-Learn |
| Reinforcement Learning | TensorFlow / Keras |
| Visualization | Matplotlib |
