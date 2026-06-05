Markdown
#  Hướng Dẫn Cài Đặt Hệ Thống Data Pipeline (Crypto Project)

Dự án này cung cấp hạ tầng dữ liệu hoàn chỉnh bao gồm kho lưu trữ (MinIO), hệ thống xử lý dữ liệu lớn (PySpark), cơ sở dữ liệu (PostgreSQL) và hệ thống điều phối tự động (Apache Airflow) để cào dữ liệu thị trường Crypto theo thời gian thực.

## 1. Yêu cầu hệ thống (Prerequisites)
* Đã cài đặt **Docker** và **Docker Desktop** (đảm bảo Docker Engine đang chạy).
* Đã cài đặt **Git** để clone mã nguồn.

## 2. Các bước khởi chạy hệ thống
**Bước 1:** Clone kho mã nguồn về máy cá nhân:
```bash
git clone <đường-link-github-của-nhóm-bạn>
cd bigdata-lab
Bước 2: Khởi chạy toàn bộ cụm Server chỉ với 1 câu lệnh (lần đầu tiên có thể mất 3-5 phút để tải Image):

Bash
docker compose up -d
Bước 3: Kiểm tra xem các container đã chạy thành công chưa:

Bash
docker ps
(Nếu thấy 4 container minio_storage, postgres_db, pyspark-jupyter và airflow_scheduler hiển thị trạng thái "Up" là thành công).

3. Thông tin truy cập các dịch vụ (Services Access)
Sau khi hệ thống chạy, bạn có thể truy cập các dịch vụ qua trình duyệt:

 Kho lưu trữ MinIO (Data Lakehouse)
Đường dẫn: http://localhost:9001

Username: admin

Password: password123

Chức năng: Chứa bucket crypto-raw-data lưu trữ các file CSV dữ liệu thô cào từ sàn Bitstamp (Cập nhật realtime).

 Apache Airflow (Điều phối tự động)
Đường dẫn: http://localhost:8080 (hoặc http://127.0.0.1:8080)

Username: admin

Password: Chạy lệnh dưới đây trong Terminal để lấy mật khẩu bảo mật ngẫu nhiên:
docker exec -it airflow_scheduler cat standalone_admin_password.txt

Chức năng: Bật/Tắt các luồng DAG cào dữ liệu.

 Jupyter Notebook (Môi trường PySpark ETL)
Đường dẫn: http://localhost:8888

Mật khẩu/Token: Chạy lệnh dưới đây để lấy đường link đăng nhập chứa token:
docker logs pyspark-jupyter (Tìm dòng có chữ http://127.0.0.1:8888/lab?token=...)

 PostgreSQL (Kho dữ liệu cấu trúc)
Host: localhost | Port: 5432

Database: retail_db

User/Pass: admin / admin

4. Cách tắt hệ thống an toàn
Khi không làm việc nữa, để giải phóng RAM cho máy tính, hãy mở Terminal tại thư mục project và gõ:

Bash
docker compose down