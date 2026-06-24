# SV5 — Văn Khiêm Chương - 22E1020002 (Reinforcement Learning / DQN Bot / Portfolio Allocation)

## Nhiệm vụ

- Nhận dữ liệu đầu vào từ SV3 (`sv3/DA2-DATA-06/processed_data/altcoins.parquet`) gồm 15 đồng crypto.
- Thiết kế một môi trường giao dịch tùy chỉnh `CryptoTradingEnv` tuân theo mô hình Markov Decision Process (MDP) bao gồm các khái niệm State, Action, và Reward.
- Xây dựng mạng DQN (Deep Q-Network) bằng Keras/TensorFlow để huấn luyện một Agent biết phân bổ tỷ trọng danh mục đầu tư (Portfolio Allocation).
- Huấn luyện Agent với tối thiểu 50 episodes, lưu biểu đồ reward trong quá trình training.
- Đánh giá mô hình trên tập kiểm thử (backtest) và so sánh hiệu quả với chiến lược Buy & Hold về các chỉ số: Total Return, Sharpe Ratio, Max Drawdown.

## Cấu trúc thư mục

```
sv5/
├── README.md
├── DA2-RL-01/
│   ├── environment.py                 # Định nghĩa lớp CryptoTradingEnv (State, Action, Reward)
│   └── mo_ta_state_action_reward.md   # Tài liệu mô tả chi tiết thiết kế Environment
├── DA2-RL-02/
│   ├── DA2_RL_02_DQN_Agent.ipynb      # Notebook thiết lập DQN Agent, ReplayMemory và training loop
│   └── ket_qua_training.md            # Đánh giá và nhận xét quá trình training
└── DA2-RL-03/
    ├── DA2_RL_03_Evaluation.ipynb     # Notebook đánh giá hiệu năng backtest so với Buy & Hold
    ├── portfolio_value.png            # Biểu đồ giá trị danh mục đầu tư so sánh
    └── bang_ket_qua_so_sanh.md        # Bảng tổng hợp kết quả đối chiếu giữa Bot và Buy & Hold
```

## Issues

| Issue | Mô tả | Trạng thái |
|-------|-------|-----------|
| DA2-RL-01 | Thiết kế Environment cho bot giao dịch crypto | 🔄 In progress |
| DA2-RL-02 | Xây dựng DQN Agent bằng Keras/TensorFlow | 🔄 In progress |
| DA2-RL-03 | Đánh giá bot và so sánh với Buy & Hold | 🔄 In progress |

## Cách chạy notebook

Chạy theo thứ tự trên Jupyter (http://localhost:8888):

1. **Khởi động môi trường và kiểm tra dữ liệu đầu vào.**
2. **Chạy `DA2-RL-02/DA2_RL_02_DQN_Agent.ipynb`** để thực hiện huấn luyện DQN Agent và tạo ra checkpoint / biểu đồ học tập.
3. **Chạy `DA2-RL-03/DA2_RL_03_Evaluation.ipynb`** để tải mô hình đã huấn luyện, thực hiện backtest và tạo biểu đồ so sánh `portfolio_value.png`.

## Input / Output

| | Đường dẫn | Chi tiết |
|---|---|---|
| **Input** | `/home/jovyan/work/sv3/DA2-DATA-06/processed_data/altcoins.parquet` | Chứa dữ liệu lịch sử giá của 15 đồng crypto |
| **Coins** | `ETH, XRP, LTC, LINK, UNI, MATIC, SOL, ADA, DOT, AVAX, DOGE, SHIB, BCH, ALGO, AAVE` | Danh sách 15 đồng crypto được giao dịch |
| **State** | Ma trận giá trị lợi nhuận lịch sử (historical returns) hoặc tương quan trong khung thời gian `window_size` | Kích thước: `(window_size, num_coins)` |
| **Action** | Vector tỷ trọng phân bổ vào 15 đồng coin (cộng thêm 1 phần tiền mặt mặt định hoặc phân bổ 100% vào coins, tổng tỷ trọng = 1) | Kích thước: `(num_coins,)` hoặc số lượng danh mục hữu hạn |
| **Reward** | Sharpe Ratio hoặc lợi nhuận điều chỉnh theo rủi ro (Risk-adjusted return) | Đo lường hiệu quả phân bổ |
