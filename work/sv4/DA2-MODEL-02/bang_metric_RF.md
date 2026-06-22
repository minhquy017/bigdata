# Bảng Metric — Random Forest Classifier

**Tập test:** 198 mẫu (20% dữ liệu, theo thứ tự thời gian)

## Classification Report

| Nhãn     | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Sell (0) | 0.85      | 0.22   | 0.35     | 78      |
| Buy  (1) | 0.66      | 0.97   | 0.79     | 120     |

## Tổng hợp

| Metric             | Giá trị |
|--------------------|---------|
| Accuracy           | 0.6768  |
| Macro Avg Precision | 0.75   |
| Macro Avg Recall   | 0.60    |
| Macro Avg F1-Score | 0.57    |
| Weighted Avg F1    | 0.61    |

## Nhận xét

- Recall Buy = 0.97: bắt được 97% tín hiệu mua thực sự, rất tốt cho bài toán giao dịch.
- Recall Sell = 0.22: mô hình bỏ sót nhiều tín hiệu bán.
- Mô hình thiên về dự đoán Buy do dữ liệu hơi mất cân bằng (Buy 52.6% vs Sell 47.4%).
