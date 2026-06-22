# Nhận xét Trực quan — t-SNE Visualization

**Input:** X_svd (990 × 5 components sau TruncatedSVD)
**Output:** X_tsne (990 × 2 dimensions)
**Tham số:** perplexity=30, max_iter=1000, init='pca', random_state=42

## Kết quả centroid

| Nhóm      | Centroid (x, y)   |
|-----------|-------------------|
| Buy  (1)  | (4.88,  5.21)     |
| Sell (0)  | (-6.24, -0.37)    |
| **Khoảng cách centroid** | **12.44** |

## Nhận xét

1. **Tách biệt rõ ràng:** Khoảng cách centroid 12.44 cho thấy hai nhóm Buy và Sell có xu hướng tách biệt trong không gian 2D — t-SNE phân tách được cụm tín hiệu.

2. **Phân bố không gian:**
   - Nhóm Buy (label=1) tập trung về phía góc phần tư dương (x > 0, y > 0).
   - Nhóm Sell (label=0) tập trung về phía âm (x < 0).

3. **Vùng chồng lấp:** Vẫn có sự chồng lấp ở vùng biên giữa hai nhóm, phản ánh tính phi tuyến và nhiễu của dữ liệu thị trường crypto — giải thích tại sao Accuracy mô hình chưa đạt 100%.

4. **Tương quan với RSI:** Biểu đồ tô màu theo RSI cho thấy:
   - Vùng RSI cao (>70, màu xanh) tương ứng với nhóm Buy.
   - Vùng RSI thấp (<30, màu đỏ) tương ứng nhóm Sell.
   - Nhất quán với định nghĩa label từ MA10/MA60, xác nhận tính hợp lệ của feature engineering từ SV3.

5. **Kết luận:** t-SNE xác nhận rằng 5 chỉ báo kỹ thuật sau SVD mang đủ thông tin để phân biệt tín hiệu Buy/Sell trong không gian 2D.
