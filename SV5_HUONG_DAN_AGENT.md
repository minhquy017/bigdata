# Hướng dẫn Agent tự động triển khai SV5 — Reinforcement Learning / DQN Bot

> **Mục đích:** File này hướng dẫn AI Agent thực hiện toàn bộ công việc của SV5 một cách tự động:
> tạo cấu trúc thư mục, viết notebook, tạo issues trên AKA Hub, upload sản phẩm và cập nhật tiến độ.

---

## BƯỚC 0 — Thông tin cần hỏi người dùng trước khi bắt đầu

Agent phải hỏi người dùng cung cấp các thông tin sau (KHÔNG tiếp tục nếu chưa có đủ):

```
1. Tên đăng nhập AKA Hub (Redmine): _______________
2. Mật khẩu AKA Hub:               _______________
3. Họ và tên đầy đủ:               Văn Khiêm Chương
4. MSSV:                           22E1020002
5. Docker đang chạy chưa? (yes/no): _______________
   - Nếu chưa: chạy lệnh: docker compose up -d
     (tại thư mục bigdata/)
```

> **Lưu ý bảo mật:** Không lưu mật khẩu vào bất kỳ file nào trong project.

---

## BƯỚC 1 — Kiểm tra môi trường

Agent kiểm tra các điều kiện sau:

```bash
# 1. Kiểm tra Docker
docker ps

# Phải thấy 4 container: pyspark-jupyter, minio_storage, postgres_db, airflow_scheduler
# Nếu chưa chạy:
docker compose up -d

# 2. Lấy Jupyter token
docker logs pyspark-jupyter 2>&1 | grep "token=" | tail -2

# 3. Kiểm tra dữ liệu altcoins từ SV3 (input cho SV5)
ls "work/sv3/DA2-DATA-06/processed_data/"
# Phải có: bitcoin.parquet, altcoins.parquet
```

---

## BƯỚC 2 — Tạo cấu trúc thư mục SV5

Tạo đúng theo cấu trúc sau (giống sv3, sv4):

```
work/sv5/
├── README.md                          ← Agent tạo
├── DA2-RL-01/                         ← Issue: Thiết kế Environment
│   ├── environment.py                 ← Agent viết
│   └── mo_ta_state_action_reward.md   ← Agent viết
├── DA2-RL-02/                         ← Issue: DQN Agent
│   ├── DA2_RL_02_DQN_Agent.ipynb      ← Agent viết
│   └── ket_qua_training.md            ← Agent viết sau khi chạy notebook
└── DA2-RL-03/                         ← Issue: Đánh giá & So sánh
    ├── DA2_RL_03_Evaluation.ipynb     ← Agent viết
    ├── portfolio_value.png            ← Sinh ra khi chạy notebook
    └── bang_ket_qua_so_sanh.md        ← Agent viết sau khi chạy notebook
```

**Lệnh tạo thư mục:**
```bash
mkdir -p work/sv5/DA2-RL-01
mkdir -p work/sv5/DA2-RL-02
mkdir -p work/sv5/DA2-RL-03
```

---

## BƯỚC 3 — Nội dung từng file cần tạo

### 3.1 — work/sv5/README.md

Nội dung README theo mẫu sv4, thay thông tin SV5:
- Tên: **SV5 — Văn Khiêm Chương - 22E1020002**
- Vai trò: Reinforcement Learning / DQN Bot / Portfolio Allocation
- Input: `sv3/DA2-DATA-06/processed_data/altcoins.parquet` (15 đồng crypto)
- Issues: DA2-RL-01, DA2-RL-02, DA2-RL-03
- Thứ tự chạy: DA2-RL-01 → DA2-RL-02 → DA2-RL-03

---

### 3.2 — DA2-RL-01/environment.py

File Python (không phải notebook) định nghĩa môi trường giao dịch.

**Yêu cầu bắt buộc:**
```python
# Cấu trúc OOP — KHÔNG viết flat script
class CryptoTradingEnv:
    """
    State  : ma trận tương quan hoặc đặc trưng giá của 15 đồng crypto
    Action : vector tỷ trọng phân bổ vào các đồng coin (tổng = 1)
    Reward : Sharpe Ratio hoặc lợi nhuận điều chỉnh theo rủi ro
    """
    def __init__(self, df, window_size=10): ...
    def reset(self): ...           # trả về state ban đầu
    def step(self, action): ...    # trả về (next_state, reward, done, info)
    def _get_state(self): ...      # tính state từ dữ liệu hiện tại
    def _get_reward(self): ...     # tính reward (Sharpe hoặc return)
```

**Input:** `altcoins.parquet` từ `/home/jovyan/work/sv3/DA2-DATA-06/processed_data/altcoins.parquet`

---

### 3.3 — DA2-RL-01/mo_ta_state_action_reward.md

File mô tả thiết kế Environment:

```markdown
# Mô tả State, Action, Reward — DA2-RL-01

## State
...

## Action
...

## Reward
...

## Dữ liệu
- File: altcoins.parquet
- 15 đồng crypto: ETH, XRP, LTC, LINK, UNI, MATIC, SOL, ADA, DOT, AVAX,
                  DOGE, SHIB, BCH, ALGO, AAVE
```

---

### 3.4 — DA2-RL-02/DA2_RL_02_DQN_Agent.ipynb

Notebook Jupyter gồm các phần:

**Cell 1 — Import:**
```python
import numpy as np, pandas as pd
import tensorflow as tf
from tensorflow import keras
from collections import deque
import random, os
```

**Cell 2 — Load dữ liệu:**
```python
df = pd.read_parquet('/home/jovyan/work/sv3/DA2-DATA-06/processed_data/altcoins.parquet')
```

**Cell 3 — Class ReplayMemory:**
```python
class ReplayMemory:
    def __init__(self, capacity=10000): ...
    def push(self, state, action, reward, next_state, done): ...
    def sample(self, batch_size): ...
```

**Cell 4 — Class DQNAgent:**
```python
class DQNAgent:
    def __init__(self, state_size, action_size): ...
    def build_model(self): ...        # Q-Network bằng Keras
    def act(self, state, epsilon): ... # epsilon-greedy
    def train(self, memory, batch_size=32): ...
    def update_target(self): ...
```

**Cell 5 — Training Loop:**
```python
env = CryptoTradingEnv(df)
agent = DQNAgent(state_size=..., action_size=15)
# Chạy ít nhất 50 episodes
for episode in range(50):
    ...
```

**Cell 6 — Vẽ training reward:**
```python
plt.plot(rewards_per_episode)
plt.title('Reward qua các Episode')
plt.savefig('/home/jovyan/work/sv5/DA2-RL-02/training_reward.png')
```

---

### 3.5 — DA2-RL-03/DA2_RL_03_Evaluation.ipynb

Notebook đánh giá bot:

**Cell 1 — Load model đã train, chạy trên tập test**

**Cell 2 — Tính portfolio value qua từng bước**

**Cell 3 — So sánh với Buy & Hold:**
```python
# Chiến lược Buy & Hold: mua đều 15 đồng từ đầu, giữ đến cuối
```

**Cell 4 — Vẽ biểu đồ:**
```python
plt.plot(bot_portfolio, label='DQN Bot')
plt.plot(buyhold_portfolio, label='Buy & Hold')
plt.savefig('/home/jovyan/work/sv5/DA2-RL-03/portfolio_value.png')
```

**Cell 5 — Bảng kết quả:**
```python
# In ra: Total Return, Sharpe Ratio, Max Drawdown
```

---

## BƯỚC 4 — Chạy notebook trên Jupyter

Thứ tự chạy:
1. Mở http://localhost:8888 (dùng token từ Bước 1)
2. Chạy `sv5/DA2-RL-02/DA2_RL_02_DQN_Agent.ipynb` — Kernel → Restart & Run All
3. Chạy `sv5/DA2-RL-03/DA2_RL_03_Evaluation.ipynb` — Kernel → Restart & Run All

> **Lưu ý:** DQN training ~50 episodes có thể mất 5-10 phút.

---

## BƯỚC 5 — Tạo issues trên AKA Hub (Redmine)

**Thông tin project:**
- URL: `https://hub.aka.vn`
- Project ID: `khai_pha_du_lieu_lon_k3`
- Assignee: Văn Khiêm Chương (tìm user ID bằng API trước)

**Lấy user ID:**
```python
import urllib.request, json, base64
token = base64.b64encode(b"<USERNAME>:<PASSWORD>").decode()
req = urllib.request.Request(
    "https://hub.aka.vn/users/current.json",
    headers={"Authorization": f"Basic {token}"}
)
with urllib.request.urlopen(req) as r:
    user = json.loads(r.read())
user_id = user["user"]["id"]
```

**Tracker IDs cần dùng:**
| Tracker | ID |
|---------|-----|
| Model   | 9   |
| Weekly Report | 13 |

### 3 Issues cần tạo:

**DA2-RL-01** (Tracker: Model, 6h):
```
Subject : DA2-RL-01 - Thiết kế Environment cho bot giao dịch crypto
Mục tiêu:
- Viết class CryptoTradingEnv.
- Xác định State, Action, Reward.
- State: ma trận tương quan hoặc đặc trưng thị trường 15 đồng crypto.
- Action: vector tỷ trọng phân bổ vào các đồng coin.
- Reward: Sharpe Ratio hoặc lợi nhuận điều chỉnh theo rủi ro.

Sản phẩm cần nộp:
- environment.py (đính kèm).
- mo_ta_state_action_reward.md (đính kèm).
```

**DA2-RL-02** (Tracker: Model, 8h):
```
Subject : DA2-RL-02 - Xây dựng DQN Agent bằng Keras/TensorFlow
Mục tiêu:
- Viết class DQNAgent với Q-Network bằng Keras.
- Viết class ReplayMemory.
- Cài đặt epsilon-greedy action selection.
- Chạy training loop ít nhất 50 episodes.

Sản phẩm cần nộp:
- DA2_RL_02_DQN_Agent.ipynb (đính kèm).
- training_reward.png (đính kèm).
- ket_qua_training.md (đính kèm).
```

**DA2-RL-03** (Tracker: Model, 6h):
```
Subject : DA2-RL-03 - Đánh giá bot và so sánh với Buy & Hold
Mục tiêu:
- Chạy DQN Bot trên tập test.
- Tính Total Return, Sharpe Ratio, Max Drawdown.
- So sánh với chiến lược Buy & Hold.
- Vẽ biểu đồ portfolio value.

Sản phẩm cần nộp:
- DA2_RL_03_Evaluation.ipynb (đính kèm).
- portfolio_value.png (đính kèm).
- bang_ket_qua_so_sanh.md (đính kèm).
```

---

## BƯỚC 6 — Upload sản phẩm lên từng issue

Sau khi chạy notebook xong, upload từng file vào đúng issue:

| Issue | File cần upload |
|-------|----------------|
| DA2-RL-01 | `environment.py` + `mo_ta_state_action_reward.md` |
| DA2-RL-02 | `DA2_RL_02_DQN_Agent.ipynb` + `training_reward.png` + `ket_qua_training.md` |
| DA2-RL-03 | `DA2_RL_03_Evaluation.ipynb` + `portfolio_value.png` + `bang_ket_qua_so_sanh.md` |

**API upload file:**
```python
# Bước 1: upload binary → lấy token
def upload_file(filepath, filename, auth_token):
    with open(filepath, "rb") as f:
        data = f.read()
    req = urllib.request.Request(
        f"https://hub.aka.vn/uploads.json?filename={urllib.parse.quote(filename)}",
        data=data,
        headers={"Authorization": f"Basic {auth_token}",
                 "Content-Type": "application/octet-stream"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["upload"]["token"]

# Bước 2: đính kèm vào issue
def attach_to_issue(issue_id, upload_token, filename, notes, auth_token):
    payload = json.dumps({
        "issue": {
            "notes": notes,
            "uploads": [{"token": upload_token, "filename": filename,
                         "content_type": "application/octet-stream"}]
        }
    }).encode("utf-8")
    req = urllib.request.Request(
        f"https://hub.aka.vn/issues/{issue_id}.json",
        data=payload,
        headers={"Authorization": f"Basic {auth_token}",
                 "Content-Type": "application/json; charset=utf-8"},
        method="PUT"
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status
```

---

## BƯỚC 7 — Cập nhật description và Resolved

Sau khi upload xong, cập nhật description từng issue với kết quả thực tế (giống sv4):
```python
# PUT /issues/{id}.json với {"issue": {"description": "...", "status_id": 3, "done_ratio": 100}}
# status_id = 3 → Resolved
```

---

## BƯỚC 8 — Cập nhật tiến độ cá nhân

Thêm comment vào từng issue theo mẫu (Section 6 của doc):
```
Ngày cập nhật: DD/MM/2026
Thời gian đã làm: X giờ

Công việc đã hoàn thành:
- ...

Công việc đang làm:
- Hoàn thành.

Vấn đề gặp phải:
- ...

Link sản phẩm:
- GitHub: https://github.com/minhquy017/bigdata
- Notebook: work/sv5/DA2-RL-0X/...

Kế hoạch tiếp theo:
- ...
```

---

## BƯỚC 9 — Cập nhật DA2-G4-WEEK-03 (#14838)

Cập nhật mục 2 (SV5) trong Weekly Report tuần 3 với tiến độ thực tế:
```python
# PUT /issues/14838.json
# Cập nhật description, thêm tiến độ SV5 vào mục 2 và 3/4
```

---

## BƯỚC 10 — Git commit

```bash
cd bigdata/
git add work/sv5/
git commit -m "sv5: Reinforcement Learning DQN Bot - DA2-RL-01, RL-02, RL-03"
```

> **Chưa push** — đợi nhóm trưởng (SV1) xác nhận trước khi push lên GitHub.

---

## Checklist Agent

Đánh dấu từng bước sau khi hoàn thành:

- [ ] Hỏi thông tin người dùng (credentials AKA Hub, Docker status)
- [ ] Kiểm tra Docker + Jupyter token
- [ ] Tạo thư mục sv5/ và các issue folders
- [ ] Viết README.md sv5
- [ ] Viết environment.py (DA2-RL-01)
- [ ] Viết mo_ta_state_action_reward.md
- [ ] Viết DA2_RL_02_DQN_Agent.ipynb
- [ ] Viết DA2_RL_03_Evaluation.ipynb
- [ ] Chạy notebook trên Jupyter và lưu output
- [ ] Tạo 3 issues trên AKA Hub (DA2-RL-01, 02, 03)
- [ ] Upload tất cả file lên đúng issue
- [ ] Cập nhật description + Resolved trên từng issue
- [ ] Thêm comment tiến độ cá nhân (Section 6)
- [ ] Cập nhật DA2-G4-WEEK-03 (#14838)
- [ ] Git commit
