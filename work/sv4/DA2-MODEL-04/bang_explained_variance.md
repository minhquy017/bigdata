# Bảng Explained Variance — TruncatedSVD

**Input:** 990 mẫu × 7 features (sau StandardScaler)
**Output:** 990 mẫu × 5 components

## Explained Variance Ratio từng Component

| Component   | Explained Variance | Tỷ lệ (%) | Cumulative (%) |
|-------------|-------------------|-----------|----------------|
| Component 1 | 0.5294            | 52.94%    | 52.94%         |
| Component 2 | 0.3797            | 37.97%    | 90.91%         |
| Component 3 | 0.0472            | 4.72%     | 95.63%         |
| Component 4 | 0.0278            | 2.78%     | 98.41%         |
| Component 5 | 0.0115            | 1.15%     | 99.56%         |
| **Tổng**    | **0.9956**        | **99.56%**| —              |

## So sánh RF trước và sau SVD

| Tập dữ liệu           | Accuracy | F1-Score |
|-----------------------|----------|----------|
| Gốc (7 features)      | 0.6768   | 0.7852   |
| Sau SVD (5 components)| 0.6667   | 0.7295   |

## Nhận xét

- 5 components giải thích được **99.56%** variance của dữ liệu gốc → giảm chiều hiệu quả mà gần như không mất thông tin.
- Component 1 và 2 chiếm ~91% variance — phần lớn thông tin tập trung ở 2 chiều đầu tiên.
- Sau SVD, Accuracy giảm nhẹ 0.0101 và F1 giảm 0.0557 — đánh đổi nhỏ để đổi lấy giảm chiều từ 7 → 5.
- Dữ liệu sau giảm chiều lưu tại: `sv4/shared/X_svd.npy` (shape: 990 × 5).
