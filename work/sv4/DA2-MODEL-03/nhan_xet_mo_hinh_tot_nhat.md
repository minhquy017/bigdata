# Nhận xét Mô hình Tốt nhất — DA2-MODEL-03

## Bảng so sánh Random Forest vs Gradient Boosting

**Tập test:** 198 mẫu (20% dữ liệu, theo thứ tự thời gian)

| Mô hình           | Accuracy | Precision | Recall | F1-Score |
|-------------------|----------|-----------|--------|----------|
| Random Forest     | 0.6768   | 0.6573    | 0.9750 | 0.7852   |
| Gradient Boosting | 0.5253   | 0.5985    | 0.6583 | 0.6270   |

## Kết luận: Mô hình tốt nhất là Random Forest

**Lý do:**

1. **F1-Score cao hơn rõ rệt:** Random Forest đạt F1 = 0.7852 so với Gradient Boosting 0.6270 (chênh lệch ~15%).
2. **Recall vượt trội:** Recall = 0.9750 — bắt được 97.5% tín hiệu Buy thực sự, giảm thiểu bỏ lỡ cơ hội mua trong giao dịch crypto.
3. **Accuracy cao hơn:** 0.6768 so với 0.5253 của Gradient Boosting.

**Gradient Boosting phù hợp hơn khi:**
- Cần giảm False Positive (dự đoán Buy nhưng thực tế là Sell).
- Dữ liệu có nhiều nhiễu và cần regularization mạnh hơn.

**Quyết định:** Dùng Random Forest cho các bước tiếp theo (SVD, t-SNE).
