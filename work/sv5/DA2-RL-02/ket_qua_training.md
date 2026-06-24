# Kết quả Training — DA2-RL-02

## Thông số training

- Số episode: 50
- Episode length: 60 bước
- Batch size: 32
- Epsilon: 1.0 → 0.218 (decay 0.97/episode)
- Gamma: 0.99
- Reward function: Differential Sharpe Ratio Reward

---

## Kết quả

- Reward episode đầu: `7.1974`
- Reward episode cuối: `21.7575`

### Portfolio Value 5 Episode Cuối

| Episode | Portfolio Value |
|----------|----------|
| 46 | 1.0367 |
| 47 | 0.7558 |
| 48 | 1.2087 |
| 49 | 0.6610 |
| 50 | 0.8603 |

- Portfolio value trung bình 5 episode cuối:

```text
(1.0367 + 0.7558 + 1.2087 + 0.6610 + 0.8603) / 5
= 0.9045
```

→ **0.9045**

### Diễn biến Reward

- Reward biến động khá mạnh giữa các episode.
- Một số episode đạt reward rất cao:

| Episode | Reward |
|----------|----------|
| 14 | 215.49 |
| 20 | 163.96 |
| 21 | 291.02 |
| 42 | 54.92 |
| 43 | 47.75 |

- Một số episode có reward âm:

| Episode | Reward |
|----------|----------|
| 25 | -41.15 |
| 26 | -68.94 |
| 44 | -90.03 |
| 46 | -97.75 |

- Trên biểu đồ training xuất hiện một outlier rất lớn tại Episode 5 với reward khoảng **-7600**, làm lệch thang đo của đồ thị.
- Sau Episode 10, reward chủ yếu dao động trong khoảng từ **-100 đến 300**, không còn xuất hiện các giá trị cực đoan như giai đoạn đầu.

---

## Nhận xét

### 1. Khả năng học của Agent

- Agent đã học được một số chiến lược giao dịch có lợi nhuận vì reward cuối cùng dương (`21.7575`).
- Tuy nhiên reward chưa hội tụ rõ ràng.
- Sau Episode 20, reward vẫn dao động mạnh giữa các giá trị âm và dương, cho thấy quá trình học vẫn chưa ổn định.

### 2. Hiệu quả danh mục đầu tư

- Portfolio value dao động đáng kể từ khoảng `0.55` đến `1.50`.
- Giá trị trung bình của 5 episode cuối là `0.9045`, thấp hơn vốn ban đầu (`1.0`).
- Điều này cho thấy agent chưa tạo được hiệu suất đầu tư ổn định trên tập dữ liệu huấn luyện.

### 3. Đánh giá mức độ hội tụ

- Chưa xuất hiện xu hướng tăng trưởng reward liên tục theo số episode.
- Reward dao động mạnh là điều có thể chấp nhận được trong giai đoạn đầu huấn luyện do:
  - Epsilon-greedy vẫn còn hoạt động (`ε ≈ 0.22` ở cuối training).
  - Điểm bắt đầu mỗi episode được chọn ngẫu nhiên.
  - Dữ liệu thị trường crypto có độ biến động cao.

### 4. Đánh giá tổng thể

- DQN Agent đã học được các tín hiệu giao dịch cơ bản.
- Mô hình chưa hội tụ hoàn toàn sau 50 episode.
- Hiệu quả danh mục đầu tư chưa ổn định.
- Cần tăng số lượng episode (100–300 episode) và tiếp tục tinh chỉnh siêu tham số để cải thiện hiệu suất.

---

## Vấn đề gặp phải

### Reward Outlier

- Xuất hiện một reward âm rất lớn (~`-7600`) tại Episode 5.
- Nguyên nhân có thể đến từ tính toán Differential Sharpe Ratio khi phương sai lợi nhuận quá nhỏ ở giai đoạn đầu huấn luyện.
- Khi giá trị `(B - A²)` tiến gần về 0, reward có thể tăng hoặc giảm đột biến.

### Giải pháp áp dụng

Trong hàm `_get_reward()` đã bổ sung ngưỡng tối thiểu cho phương sai:

```python
variance = max(B - A**2, 1e-8)
```

hoặc:

```python
denominator = np.sqrt(max(B - A**2, 1e-8))
```

Giải pháp này giúp tránh hiện tượng chia cho giá trị quá nhỏ, từ đó giảm khả năng xuất hiện các reward cực lớn hoặc cực nhỏ bất thường.

---

## Kết luận

Sau 50 episode huấn luyện, DQN Agent sử dụng Differential Sharpe Ratio Reward đã học được một số hành vi giao dịch có lợi nhuận, thể hiện qua reward cuối cùng dương (`21.7575`). Tuy nhiên reward và portfolio value vẫn biến động mạnh giữa các episode, cho thấy mô hình chưa hội tụ hoàn toàn và chưa đạt được hiệu quả đầu tư ổn định. Trong các thí nghiệm tiếp theo, cần tăng số lượng episode huấn luyện, cải thiện reward function và tinh chỉnh siêu tham số để nâng cao hiệu suất quản lý danh mục đầu tư.