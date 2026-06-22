# PROJECT PLAN
# ĐỒ ÁN 2: PIPELINE DỮ LIỆU GIAO DỊCH TIỀN ĐIỆN TỬ (CRYPTO) VÀ BOT RL

## 1. MỤC TIÊU DỰ ÁN

Mục tiêu của dự án là xây dựng hệ thống xử lý dữ liệu giao dịch Crypto kết hợp Machine Learning và Reinforcement Learning nhằm hỗ trợ dự đoán tín hiệu Buy/Sell và tối ưu hóa phân bổ danh mục đầu tư.

---

## 2. TIMELINE DỰ ÁN (1 THÁNG)

| Tuần | Mục tiêu | Thành viên | Deliverables |
|------|-----------|------------|---------------|
| Tuần 1 | Setup môi trường, dataset, requirement | Dân, Quý | Docker, MinIO, Requirement |
| Tuần 2 | ETL + Feature Engineering | Hiếu | Technical Indicators |
| Tuần 3 | Machine Learning + SVD + t-SNE | Khánh | Buy/Sell Model |
| Tuần 4 | RL Bot + Báo cáo + Demo | Chương, Dân | DQN Bot, Slide |

---

## 3. KẾ HOẠCH CHI TIẾT

### TUẦN 1 – SETUP & REQUIREMENT

**Mục tiêu:**
- Đọc yêu cầu đồ án
- Tạo GitHub / Google Drive
- Setup Docker, MinIO
- Thu thập dataset crypto
- Upload dữ liệu

**Output:**
- requirement.md
- compose.yaml
- Dataset Crypto
- Weekly Report tuần 1

---

### TUẦN 2 – ETL & FEATURE ENGINEERING

**Mục tiêu:**
- Đọc dữ liệu từ MinIO
- Làm sạch dữ liệu
- Xử lý missing values
- Tính indicators

**Output:**
- ETL Notebook
- Feature Table
- Label Buy/Sell

---

### TUẦN 3 – MACHINE LEARNING

**Mục tiêu:**
- Train Random Forest
- Train Gradient Boosting
- StandardScaler
- TruncatedSVD
- t-SNE

**Output:**
- Buy/Sell Notebook
- Confusion Matrix
- t-SNE Visualization

---

### TUẦN 4 – RL & FINALIZATION

**Mục tiêu:**
- DQN Agent
- Environment
- Portfolio Evaluation
- Slide
- Video Demo

**Output:**
- RL Notebook
- Final Report
- README
- Slide
- Demo Video

---

## 4. RISK MANAGEMENT

| Rủi ro | Mức độ | Giải pháp |
|--------|--------|------------|
| Docker lỗi | Trung bình | Setup backup |
| Spark lỗi MinIO | Trung bình | Kiểm tra S3A |
| DQN quá khó | Cao | Prototype trước |
| Trễ deadline | Cao | Chia task nhỏ |

---

## 5. KPI DỰ ÁN

- Tuần 1: Hoàn thành setup môi trường
- Tuần 2: Hoàn thành feature engineering
- Tuần 3: Hoàn thành ML + Visualization
- Tuần 4: Hoàn thành RL + báo cáo + demo
