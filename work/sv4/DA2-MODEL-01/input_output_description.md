# Mô tả Input / Output — DA2-MODEL-01

## Input

| Thông tin | Giá trị |
|-----------|---------|
| File | `sv3/DA2-DATA-06/processed_data/bitcoin.parquet` |
| Tổng số mẫu | 990 dòng |
| Số cột | 14 cột |
| Khoảng thời gian | từ 2026-06-10 23:46:00 (dữ liệu 1 phút) |

**Các cột trong file:**
`timestamp, open, high, low, close, volume, MA10, MA60, ROC, MOM, RSI, stoch_k, stoch_d, label`

**Features (X) — 7 chỉ báo kỹ thuật:**

| Feature | Mô tả |
|---------|-------|
| MA10 | Moving Average 10 nến |
| MA60 | Moving Average 60 nến |
| ROC | Rate of Change |
| MOM | Momentum |
| RSI | Relative Strength Index (14 kỳ) |
| stoch_k | Stochastic %K |
| stoch_d | Stochastic %D |

**Target (y):**
- `label = 1` → Buy  (MA10 > MA60)
- `label = 0` → Sell (MA10 ≤ MA60)

**Phân bố label:**
- Buy  (1): 521 mẫu (52.6%)
- Sell (0): 469 mẫu (47.4%)
- Missing values: 0 (không có dữ liệu thiếu)

---

## Xử lý

- Sắp xếp theo `timestamp` tăng dần (không shuffle)
- Chia train/test theo thứ tự thời gian: 80% train / 20% test
- Chuẩn hóa bằng `StandardScaler` (fit trên train, transform cả hai)

---

## Output

| Tập | Số mẫu | Tỷ lệ |
|-----|--------|-------|
| Train | 792 | 80% |
| Test  | 198 | 20% |

**StandardScaler:**

| Feature | Mean | Std |
|---------|------|-----|
| MA10 | 61902.68 | 394.70 |
| MA60 | 61889.28 | 364.10 |
| ROC | 0.0074 | 0.2063 |
| MOM | 4.4857 | 127.63 |
| RSI | 50.43 | 15.04 |
| stoch_k | 50.23 | 30.41 |
| stoch_d | 50.17 | 27.83 |

**Files lưu tại `sv4/shared/`:**
- `scaler.pkl` — StandardScaler đã fit
- `X_train_sc.npy` — shape (792, 7)
- `X_test_sc.npy`  — shape (198, 7)
- `y_train.npy`    — shape (792,)
- `y_test.npy`     — shape (198,)
