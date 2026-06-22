# SV4 — Khánh (Machine Learning / SVD / t-SNE)

## Nhiệm vụ

- Nhận feature table từ SV3 (`sv3/DA2-DATA-06/processed_data/bitcoin.parquet`)
- Chia train/test theo thứ tự thời gian (không shuffle)
- Chuẩn hóa dữ liệu bằng StandardScaler
- Huấn luyện Random Forest và Gradient Boosting phân loại tín hiệu Buy/Sell
- Đánh giá mô hình: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Giảm chiều dữ liệu từ 7 indicators xuống 5 components bằng TruncatedSVD
- Trực quan hóa t-SNE để quan sát vùng tín hiệu Buy/Sell

## Cấu trúc thư mục

```
sv4/
├── README.md
└── DA2_ML_BuySell_SVD_tSNE.ipynb   # Notebook chính SV4
```

## Issues

| Issue | Mô tả | Trạng thái |
|-------|-------|-----------|
| DA2-MODEL-01 | Chuẩn bị dữ liệu train/test | 🔄 In progress |
| DA2-MODEL-02 | Huấn luyện Random Forest Classifier | 🔄 In progress |
| DA2-MODEL-03 | Huấn luyện Gradient Boosting và so sánh | 🔄 In progress |
| DA2-MODEL-04 | Chuẩn hóa + TruncatedSVD | 🔄 In progress |
| DA2-EDA-01 | Trực quan hóa t-SNE | 🔄 In progress |

## Cách chạy notebook

1. Mở Jupyter tại http://localhost:8888
2. Vào `sv4/DA2_ML_BuySell_SVD_tSNE.ipynb`
3. Run All Cells (Kernel → Restart & Run All)

> **Lưu ý:** Cell t-SNE (~30 giây) chạy sau khi SVD hoàn thành.

## Input / Output

| | Đường dẫn |
|--|-----------|
| Input | `/home/jovyan/work/sv3/DA2-DATA-06/processed_data/bitcoin.parquet` |
| Features | `MA10, MA60, ROC, MOM, RSI, stoch_k, stoch_d` |
| Target | `label` (1=Buy, 0=Sell) |
| Train/Test split | 80% / 20% theo thứ tự thời gian |

## Nội dung notebook

| Section | Mô tả |
|---------|-------|
| 1 | Import thư viện |
| 2 | Load dữ liệu từ SV3 |
| 3 | Kiểm tra dữ liệu + phân bố label |
| 4 | Split train/test + StandardScaler |
| 5 | Random Forest + Confusion Matrix |
| 6 | Gradient Boosting + Confusion Matrix |
| 7 | Bảng so sánh 2 mô hình |
| 8 | TruncatedSVD (7 → 5 components) |
| 9 | t-SNE visualization |
| 10 | So sánh trước/sau SVD |
| 11 | Tổng kết kết quả |
