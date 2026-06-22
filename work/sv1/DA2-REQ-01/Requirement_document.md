````md
# REQUIREMENT DOCUMENT
# ĐỒ ÁN 2: PIPELINE DỮ LIỆU GIAO DỊCH TIỀN ĐIỆN TỬ (CRYPTO) VÀ BOT RL

---

# THÔNG TIN ĐỒ ÁN

**Tên đề tài:**  
**Đồ án 2: Pipeline Dữ liệu Giao dịch Tiền điện tử (Crypto) và Bot RL**

**Thời gian thực hiện:** 01 tháng

**Mục tiêu thực hiện:**  
Xây dựng một hệ thống xử lý dữ liệu giao dịch tiền điện tử kết hợp Machine Learning và Reinforcement Learning nhằm hỗ trợ phân tích tín hiệu đầu tư, dự đoán Buy/Sell và tối ưu hóa phân bổ danh mục đầu tư Crypto.

---

# THÔNG TIN NHÓM

| Thành viên | Vai trò | Nhiệm vụ chính |
|------------|----------|----------------|
| Dân | SV1 – Nhóm trưởng | Requirement, quản lý tiến độ, báo cáo, slide |
| Quý | SV2 – Data Engineering | Docker, MinIO, Dataset Crypto |
| Hiếu | SV3 – ETL Engineer | PySpark, Feature Engineering, Airflow |
| Khánh | SV4 – Machine Learning Engineer | Buy/Sell Signal, SVD, t-SNE |
| Chương | SV5 – Reinforcement Learning Engineer | DQN Bot, Backtest, Demo |

---

# 1. GIỚI THIỆU ĐỀ TÀI

Trong những năm gần đây, thị trường tiền điện tử (Cryptocurrency) phát triển mạnh mẽ với khối lượng giao dịch lớn và dữ liệu thay đổi liên tục theo thời gian thực. Việc phân tích dữ liệu giao dịch nhằm đưa ra quyết định đầu tư hiệu quả trở thành một bài toán quan trọng trong lĩnh vực khoa học dữ liệu, tài chính và trí tuệ nhân tạo.

Tuy nhiên, dữ liệu giao dịch Crypto có đặc điểm là dữ liệu chuỗi thời gian (time series), khối lượng lớn, xuất hiện missing values và biến động mạnh. Điều này gây khó khăn trong quá trình lưu trữ, xử lý, khai thác và xây dựng mô hình học máy.

Do đó, nhóm thực hiện đề tài **“Pipeline Dữ liệu Giao dịch Tiền điện tử (Crypto) và Bot RL”** nhằm xây dựng một hệ thống hoàn chỉnh từ thu thập dữ liệu, xử lý dữ liệu lớn bằng PySpark, trích xuất đặc trưng kỹ thuật, huấn luyện mô hình Machine Learning cho tín hiệu Buy/Sell và xây dựng bot học tăng cường (Reinforcement Learning) hỗ trợ phân bổ danh mục đầu tư Crypto.

---

# 2. BÀI TOÁN ĐẶT RA (PROBLEM STATEMENT)

Thị trường Crypto có khối lượng dữ liệu giao dịch lớn với tốc độ cập nhật liên tục theo từng phút hoặc từng giây. Nhà đầu tư thường gặp khó khăn trong việc:

- Thu thập và quản lý dữ liệu giao dịch khối lượng lớn.
- Xử lý dữ liệu bị thiếu hoặc không đồng nhất.
- Xác định tín hiệu mua/bán hiệu quả.
- Giảm chiều dữ liệu kỹ thuật để trực quan hóa xu hướng thị trường.
- Xây dựng hệ thống hỗ trợ quyết định đầu tư tự động.

Do đó, cần xây dựng một hệ thống pipeline dữ liệu kết hợp Machine Learning và Reinforcement Learning để hỗ trợ xử lý dữ liệu, dự đoán tín hiệu giao dịch và tối ưu hóa chiến lược đầu tư.

---

# 3. MỤC TIÊU ĐỒ ÁN (OBJECTIVES)

## 3.1 Data Engineering Pipeline

- Thu thập dữ liệu Bitcoin theo phút và dữ liệu nhiều đồng Crypto khác.
- Lưu trữ dữ liệu trên MinIO.
- Xử lý dữ liệu lớn bằng PySpark.
- Chuẩn hóa dữ liệu phục vụ Machine Learning.

## 3.2 Feature Engineering

Xây dựng các technical indicators:

- MA10
- MA60
- ROC
- Momentum
- RSI
- Stochastic Oscillator

## 3.3 Machine Learning

Huấn luyện các mô hình:

- Random Forest Classifier
- Gradient Boosting Classifier

Đánh giá bằng:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 3.4 Dimensionality Reduction

- Chuẩn hóa dữ liệu bằng StandardScaler
- Áp dụng TruncatedSVD
- Trực quan hóa bằng t-SNE

## 3.5 Reinforcement Learning

- Thiết kế Environment giao dịch
- Xây dựng DQN Agent
- Portfolio Allocation
- So sánh với Buy & Hold

---

# 4. PHẠM VI ĐỒ ÁN (PROJECT SCOPE)

## 4.1 Phạm vi thực hiện

### Data Engineering
- Docker Environment
- MinIO Object Storage
- Dataset Crypto
- PySpark ETL Pipeline

### Machine Learning
- Buy/Sell Classification
- Technical Indicators
- Feature Engineering

### Data Visualization
- TruncatedSVD
- t-SNE Visualization

### Reinforcement Learning
- DQN Trading Bot
- Portfolio Allocation
- Backtesting

## 4.2 Ngoài phạm vi đồ án

Các nội dung không nằm trong phạm vi thực hiện:

- Real-time trading
- Production deployment
- Tích hợp API giao dịch thật
- Hệ thống đầu tư tự động ngoài thực tế

---

# 5. KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

```text
Crypto Dataset
      ↓
    MinIO
      ↓
PySpark ETL Pipeline
      ↓
Feature Engineering
      ↓
Buy/Sell Classification
      ↓
SVD + t-SNE
      ↓
DQN Trading Bot
      ↓
Portfolio Evaluation
````

## Mô tả hệ thống

### Bước 1 – Data Collection

* Thu thập dữ liệu Bitcoin theo phút
* Thu thập dữ liệu nhiều đồng Crypto

### Bước 2 – Data Storage

* Upload dữ liệu lên MinIO

### Bước 3 – ETL Pipeline

* Làm sạch dữ liệu
* Xử lý missing values
* Chuẩn hóa timestamp

### Bước 4 – Feature Engineering

* Tính toán technical indicators

### Bước 5 – Machine Learning

* Phân loại tín hiệu Buy/Sell

### Bước 6 – Dimensionality Reduction

* TruncatedSVD
* t-SNE

### Bước 7 – Reinforcement Learning

* Environment
* DQN Agent
* Portfolio Evaluation

---

# 6. CÔNG NGHỆ SỬ DỤNG (TECH STACK)

| Thành phần             | Công nghệ          |
| ---------------------- | ------------------ |
| Containerization       | Docker Desktop     |
| Object Storage         | MinIO              |
| Big Data Processing    | PySpark            |
| Notebook               | Jupyter Notebook   |
| Workflow               | Airflow            |
| Data Format            | Parquet / Iceberg  |
| Machine Learning       | Scikit-Learn       |
| Reinforcement Learning | TensorFlow / Keras |
| Visualization          | Matplotlib         |
| Version Control        | GitHub             |

---

# 7. FUNCTIONAL REQUIREMENTS

### FR1 – Data Collection

Hệ thống phải thu thập dữ liệu giao dịch Crypto.

### FR2 – Data Storage

Hệ thống phải lưu trữ dữ liệu trên MinIO.

### FR3 – ETL Processing

Hệ thống phải làm sạch và chuẩn hóa dữ liệu.

### FR4 – Feature Engineering

Hệ thống phải tính technical indicators.

### FR5 – Buy/Sell Classification

Hệ thống phải dự đoán tín hiệu Buy/Sell.

### FR6 – Dimensionality Reduction

Hệ thống phải hỗ trợ SVD và t-SNE.

### FR7 – Reinforcement Learning

Hệ thống phải hỗ trợ mô hình DQN.

---

# 8. NON-FUNCTIONAL REQUIREMENTS

### Hiệu năng

* Xử lý dữ liệu Crypto khối lượng lớn.

### Độ tin cậy

* Pipeline phải hoạt động ổn định.

### Khả năng mở rộng

* Hỗ trợ thêm nhiều đồng coin.

### Khả năng tái sử dụng

* Có thể tái sử dụng notebook và pipeline.

---

# 9. RISK MANAGEMENT

| Rủi ro                     | Mức độ     | Giải pháp              |
| -------------------------- | ---------- | ---------------------- |
| Spark không đọc được MinIO | Trung bình | Kiểm tra S3A connector |
| Missing values nhiều       | Trung bình | Forward Fill           |
| DQN khó hội tụ             | Cao        | Prototype trước        |
| Thiếu thời gian            | Cao        | Chia task theo tuần    |
| Accuracy thấp              | Trung bình | Hyperparameter tuning  |

---

# 10. DELIVERABLES

Nhóm cần hoàn thành:

* Docker Environment
* MinIO Storage
* Dataset Crypto
* Notebook ETL
* Technical Indicators
* Buy/Sell Classification
* Confusion Matrix
* TruncatedSVD
* t-SNE Visualization
* DQN Trading Bot
* README
* Báo cáo cuối kỳ
* Slide trình bày
* Video Demo
* GitHub Source Code

---

# 11. KẾT LUẬN

Đề tài hướng đến việc xây dựng hệ thống xử lý dữ liệu Crypto hoàn chỉnh, kết hợp giữa Data Engineering, Machine Learning và Reinforcement Learning nhằm hỗ trợ phân tích dữ liệu giao dịch và tối ưu chiến lược đầu tư. Hệ thống đáp ứng yêu cầu học thuật và có khả năng mở rộng trong các bài toán tài chính thực tế.

```
```
