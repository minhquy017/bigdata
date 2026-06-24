# Mô tả State, Action, Reward — DA2-RL-01

## Bài toán
Xây dựng môi trường RL cho bot **phân bổ vốn (portfolio allocation)** trên 15
đồng altcoin, mục tiêu tối đa hoá lợi nhuận điều chỉnh theo rủi ro (risk-adjusted
return) thay vì chỉ lợi nhuận thuần.

## State
Tại bước thời gian `t`, state là vector gồm 2 phần ghép lại:

1. **Cửa sổ log-return chuẩn hoá**: `window_size` (mặc định 10) bước gần nhất
   của log-return 15 coin, chuẩn hoá z-score theo từng coin trong chính cửa sổ
   đó → shape `(window_size, 15)`, flatten thành vector `window_size * 15`.
   Dùng log-return (không dùng giá tuyệt đối) để loại bỏ ảnh hưởng của thang
   giá khác nhau giữa các coin (ví dụ SHIB ~10⁻⁵ USD vs ETH ~10³ USD).
2. **Tỷ trọng portfolio hiện tại** (`weights`, 15 chiều): để agent biết mình
   đang nắm gì trước khi quyết định rebalance, từ đó env mới có thể tính đúng
   chi phí giao dịch (turnover).

→ `state_size = window_size * 15 + 15`.

## Action
Vector tỷ trọng phân bổ vào 15 coin, **long-only** (không bán khống), tổng = 1.
Environment tự chuẩn hoá: `clip(action, 0, None)` rồi chia tổng — nên agent có
thể đưa vào bất kỳ vector không âm nào, không cần tự lo softmax.

**Lưu ý quan trọng (khác với mô tả "thuần liên tục"):** DQN (DA2-RL-02) là
thuật toán cho không gian hành động **rời rạc**. Để dùng được DQN, ta định
nghĩa thêm một tập **action template** rời rạc (hàm `build_discrete_action_set`
trong `environment.py`):

- 15 action "tập trung": 80% vào 1 coin, 20% chia đều 14 coin còn lại.
- 1 action equal-weight (chia đều 15 coin).

→ 16 action rời rạc. DQNAgent chọn index trong tập này, map sang vector
trọng số, rồi mới gọi `env.step(weights)`. Environment bản thân vẫn nhận
action liên tục — nên nếu sau này đổi sang thuật toán continuous-control
(DDPG/PPO/SAC) thì không cần sửa lại Environment.

## Reward
**Differential Sharpe Ratio (DSR)** — Moody & Saffell, *"Reinforcement
Learning for Trading"*, NeurIPS 1998.

Sharpe Ratio chuẩn cần tính trên cả một chuỗi return (chỉ biết được ở cuối
episode) nên không dùng trực tiếp làm reward cho TD-learning từng bước được.
DSR giải quyết bằng cách duy trì 2 EMA (`A` = EMA của return, `B` = EMA của
return²) và tính "đạo hàm tức thời" của Sharpe Ratio theo return mới nhất:

```
delta_A = R_t - A_{t-1}
delta_B = R_t^2 - B_{t-1}
D_t = (B_{t-1} * delta_A - 0.5 * A_{t-1} * delta_B) / (B_{t-1} - A_{t-1}^2)^(3/2)
```

`R_t` ở đây là **portfolio log-return sau khi đã trừ phí giao dịch** —
`turnover * transaction_cost` (transaction_cost mặc định 0.001). Trừ phí
ngay trong reward để agent học được việc rebalance liên tục là có giá, tránh
hành vi "đảo danh mục" mỗi bước chỉ để né một biến động nhỏ.

## Dữ liệu
- File: `altcoins.parquet`
- Nguồn: `/home/jovyan/work/sv3/DA2-DATA-06/processed_data/altcoins.parquet`
- 15 đồng crypto: ETH, XRP, LTC, LINK, UNI, MATIC, SOL, ADA, DOT, AVAX,
  DOGE, SHIB, BCH, ALGO, AAVE
- Giả định: cột là giá đóng cửa, index là thời gian tăng dần. Nếu file có cột
  `date`/`timestamp` riêng, cần `set_index()` trước khi đưa vào `CryptoTradingEnv`.
