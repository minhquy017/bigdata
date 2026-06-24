# Bảng kết quả so sánh — DA2-RL-03

## Thông tin tập kiểm thử

- Test set: 98 dòng dữ liệu
- Số lượng tài sản: 14 đồng coin
- Số bước giao dịch thực tế: 87 bước
- Giá trị danh mục ban đầu: 1.0 (chuẩn hóa)

---

## Bảng kết quả

| Chỉ số | DQN Bot | Buy & Hold |
|----------|----------|----------|
| Total Return | -30.53% | -30.05% |
| Sharpe Ratio (annualized) | -2.990 | -3.048 |
| Max Drawdown | -37.44% | -35.21% |

---

## Kết quả cuối cùng

| Chỉ số | Giá trị |
|----------|----------|
| Portfolio Value cuối của DQN Bot | 0.6947 |
| Portfolio Value cuối của Buy & Hold | 0.6995 |
| Số bước đánh giá | 87 |

---

## Biểu đồ

Xem file `portfolio_value.png`.

Biểu đồ thể hiện diễn biến giá trị danh mục của DQN Bot và chiến lược Buy & Hold trên toàn bộ tập kiểm thử.

---

## Nhận xét

### 1. So sánh Total Return

- DQN Bot đạt Total Return **-30.53%**.
- Buy & Hold đạt Total Return **-30.05%**.

Kết quả cho thấy DQN Bot không vượt qua được chiến lược Buy & Hold về lợi nhuận cuối cùng. Chênh lệch tuy nhỏ (~0.48%) nhưng Buy & Hold vẫn đạt hiệu quả tốt hơn trong giai đoạn kiểm thử này.

### 2. So sánh Sharpe Ratio

- DQN Bot: **-2.990**
- Buy & Hold: **-3.048**

Mặc dù có lợi nhuận thấp hơn một chút, DQN Bot đạt Sharpe Ratio tốt hơn Buy & Hold.

Điều này cho thấy danh mục của DQN Bot có tỷ lệ lợi nhuận/rủi ro tốt hơn, tức là mức độ biến động được kiểm soát tốt hơn so với chiến lược nắm giữ thụ động.

### 3. So sánh Max Drawdown

- DQN Bot: **-37.44%**
- Buy & Hold: **-35.21%**

DQN Bot có mức sụt giảm vốn lớn nhất cao hơn Buy & Hold khoảng 2.23%.

Điều này cho thấy trong giai đoạn thị trường giảm mạnh, agent vẫn chưa học được chiến lược phòng thủ hiệu quả để hạn chế tổn thất.

### 4. Phân tích diễn biến danh mục

- Trong phần lớn thời gian kiểm thử, hai đường giá trị danh mục di chuyển tương đối giống nhau.
- DQN Bot đôi lúc vượt Buy & Hold ở một số giai đoạn ngắn, tuy nhiên không duy trì được lợi thế đến cuối kỳ.
- Từ khoảng bước thời gian 60 trở đi, cả hai chiến lược đều suy giảm mạnh do xu hướng thị trường bất lợi.
- Cuối giai đoạn kiểm thử, giá trị danh mục của cả hai chiến lược đều giảm xuống dưới mức vốn ban đầu.

### 5. Đánh giá tổng thể

Kết quả cho thấy DQN Bot chưa vượt qua được chiến lược Buy & Hold về lợi nhuận tuyệt đối trên tập kiểm thử hiện tại. Tuy nhiên, agent đạt Sharpe Ratio tốt hơn, cho thấy mô hình đã học được một phần đặc tính tối ưu hóa rủi ro thông qua hàm thưởng Differential Sharpe Ratio.

Do tập dữ liệu kiểm thử nằm trong giai đoạn thị trường giảm giá, cả hai chiến lược đều ghi nhận mức lợi nhuận âm đáng kể.

---

## Hạn chế

- Chỉ đánh giá trên một tập kiểm thử gồm 98 dòng dữ liệu nên chưa phản ánh đầy đủ khả năng tổng quát hóa của mô hình.
- Thị trường trong giai đoạn kiểm thử có xu hướng giảm mạnh, khiến cả DQN Bot và Buy & Hold đều đạt kết quả âm.
- Action space được rời rạc hóa thành 16 cấu hình danh mục mẫu, làm giảm khả năng phân bổ vốn linh hoạt so với các phương pháp Continuous Control (DDPG, TD3, SAC, PPO Continuous).
- Số lượng episode huấn luyện còn thấp (50 episode), có thể chưa đủ để agent hội tụ hoàn toàn.

---

## Kết luận

Trên tập kiểm thử gồm 98 dòng dữ liệu và 14 đồng coin, DQN Bot đạt Total Return **-30.53%**, Sharpe Ratio **-2.990** và Max Drawdown **-37.44%**. So với chiến lược Buy & Hold, mô hình chưa cải thiện được lợi nhuận cuối cùng nhưng đạt Sharpe Ratio tốt hơn, cho thấy agent đã học được một phần cơ chế cân bằng giữa lợi nhuận và rủi ro. Kết quả này là cơ sở để tiếp tục cải thiện mô hình bằng cách tăng thời gian huấn luyện, mở rộng tập dữ liệu và thử nghiệm các thuật toán Reinforcement Learning nâng cao hơn.