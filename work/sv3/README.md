# SV3 — Hiếu (ETL / PySpark / Feature Engineering / Airflow)

## Nhiệm vụ

- Đọc dữ liệu từ MinIO bằng PySpark qua S3A connector
- Làm sạch dữ liệu: xử lý missing values, gap theo phút, chuẩn hóa timestamp
- Tính các chỉ báo kỹ thuật (Technical Indicators)
- Tạo nhãn Buy/Sell từ MA10 và MA60
- Lưu feature table ra Parquet
- Viết Airflow DAG tự động hóa pipeline ETL

## Cấu trúc thư mục

```
sv3/
├── DA2-DATA-03/                       # Đọc dữ liệu từ MinIO
│   ├── DA2_DATA_03.ipynb              # Notebook đọc dữ liệu (S3A)
│   ├── DA2_DATA_03_2.ipynb            # Notebook đọc dữ liệu (s3fs)
│   ├── Schema_bitcoin.png             # Ảnh schema Bitcoin
│   └── Schema_altcoins.png            # Ảnh schema Altcoins
├── DA2-DATA-04/                       # Làm sạch dữ liệu
│   ├── DA2_Process_Bitcoin.ipynb      # Notebook làm sạch Bitcoin
│   ├── DA2_Process_Altcoins.ipynb     # Notebook làm sạch Altcoins
│   ├── Missing_bitcoin.png            # Thống kê missing values Bitcoin
│   ├── Missing_altcoins.png           # Thống kê missing values Altcoins
│   └── Phuong_phap_xu_ly.txt         # Ghi chú phương pháp xử lý
├── DA2-DATA-05/                       # Feature Engineering
│   ├── DA2_FE_Bitcoin.ipynb           # Notebook tính indicators Bitcoin
│   ├── DA2_FE_Altcoins.ipynb          # Notebook tính indicators Altcoins
│   └── Y_nghia_chi_bao_ky_thuat.txt  # Mô tả ý nghĩa từng chỉ báo
├── DA2-DATA-06/                       # Tạo nhãn + lưu Parquet
│   ├── DA2_Label_Save_Bitcoin.ipynb   # Notebook tạo label + lưu Bitcoin
│   ├── DA2_Label_Save_Altcoins.ipynb  # Notebook tạo label + lưu Altcoins
│   ├── Table_Bitcoin.png              # Ảnh feature table Bitcoin
│   ├── Table_Altcoins.png             # Ảnh feature table Altcoins
│   └── processed_data/
│       ├── bitcoin.parquet            # ← Input cho SV4
│       └── altcoins.parquet
└── DA2-DATA-07/                       # Airflow DAG
    └── realtime_crypto.py             # DAG tự động hóa pipeline ETL
```

## Issues

| Issue | Mô tả | Trạng thái |
|-------|-------|-----------|
| DA2-DATA-03 | Đọc dữ liệu từ MinIO bằng PySpark | ✅ 100% |
| DA2-DATA-04 | Làm sạch dữ liệu crypto và xử lý missing values | ✅ 100% |
| DA2-DATA-05 | Tính MA10, MA60, ROC, MOM, RSI và Stochastic | ✅ 100% |
| DA2-DATA-06 | Tạo nhãn Buy/Sell và lưu feature table | ✅ 100% |
| DA2-DATA-07 | Tạo Airflow DAG cho pipeline ETL | 🔄 In progress |

## Technical Indicators

| Indicator | Cột | Mô tả |
|-----------|-----|-------|
| Moving Average ngắn | `MA10` | Trung bình 10 nến |
| Moving Average dài | `MA60` | Trung bình 60 nến |
| Rate of Change | `ROC` | Tỷ lệ thay đổi giá |
| Momentum | `MOM` | Động lượng giá |
| RSI | `RSI` | Relative Strength Index (14 kỳ) |
| Stochastic %K | `stoch_k` | Vị trí giá trong range 14 nến |
| Stochastic %D | `stoch_d` | MA3 của %K |

## Nhãn Buy/Sell

```python
label = 1  # Buy  nếu MA10 > MA60
label = 0  # Sell nếu MA10 <= MA60
```

## Output cho SV4

File `DA2-DATA-06/processed_data/bitcoin.parquet` gồm các cột:
`timestamp, open, high, low, close, volume, MA10, MA60, ROC, MOM, RSI, stoch_k, stoch_d, label`
