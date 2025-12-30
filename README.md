Dưới đây là **README hoàn chỉnh – đúng yêu cầu đề bài – đúng những gì nhóm bạn đã làm từ Backend đến FE3**, viết theo phong cách **đồ án học phần / bảo vệ**, không marketing, không lan man.

Bạn có thể **copy dán nguyên file này làm `README.md`** cho repo:

---

# FSB_MSA36HN_FinalProject__Python_Group8

## Student Management & Data Analysis System

---

## 1. Giới thiệu dự án

Dự án **Student Management & Data Analysis System** được xây dựng nhằm đáp ứng yêu cầu của học phần **FSB_MSA36HN**, tập trung vào:

* Xây dựng **API Backend** quản lý thông tin sinh viên
* Phát triển **Desktop Application (FE3)** để:

  * Crawl dữ liệu từ API
  * Lưu dữ liệu ra text file
  * Tiền xử lý dữ liệu bằng Pandas
  * Phân tích và trực quan hóa dữ liệu học tập của sinh viên

Dự án áp dụng kiến trúc phân tầng rõ ràng, tận dụng sức mạnh của **Python, FastAPI, MongoDB, Pandas và PyQt5**.

---

## 2. Mô tả yêu cầu đề bài

### Yêu cầu chung:

* Mỗi sinh viên có các thông tin:

  * Mã sinh viên
  * Họ, tên
  * Email
  * Ngày sinh
  * Quê quán
  * Điểm Toán, Văn, Tiếng Anh
* Website / hệ thống có chức năng:

  * Thêm, sửa, xóa sinh viên
  * Hiển thị danh sách sinh viên
  * Dữ liệu có thể thiếu khi nhập
  * Nhập sẵn dữ liệu của 100 sinh viên

### Yêu cầu FE3 (Nhóm 8):

* API trả về thông tin sinh viên dạng JSON
* Chương trình crawl dữ liệu từ API
* Lưu dữ liệu vào text file
* Tiền xử lý dữ liệu bằng Pandas
* Phân tích và so sánh:

  * Điểm Toán / Tiếng Anh
  * Quê quán / Tiếng Anh
  * Phân bố điểm theo vùng

---

## 3. Kiến trúc tổng thể hệ thống

```
Backend (FastAPI + MongoDB)
        ↓
REST API (JSON)
        ↓
Desktop App (PyQt5)
        ↓
Crawl → Save Text File → Pandas Preprocessing → Analysis → Visualization
```

---

## 4. Công nghệ sử dụng

### Backend

* Python 3.10+
* FastAPI
* MongoDB Atlas (Cloud)
* PyMongo
* python-dotenv

### Frontend (FE3 – Desktop App)

* PyQt5
* Requests
* Pandas
* Matplotlib
* NumPy

---

## 5. Backend – FastAPI

### 5.1 Chức năng chính

* Quản lý sinh viên (CRUD)
* Cung cấp API JSON cho từng sinh viên
* Kết nối MongoDB Cloud
* Seed sẵn dữ liệu 100 sinh viên

### 5.2 Cấu trúc thư mục Backend

```
backend/
├── app/
│   ├── api/            # API endpoints
│   ├── services/       # Business logic
│   ├── repositories/   # Database access
│   ├── models/         # Data models
│   ├── core/           # Config & database
│   └── main.py         # FastAPI entry point
├── .env
└── requirements.txt
```

### 5.3 Chạy Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Truy cập Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 6. Frontend FE3 – Desktop Application

### 6.1 Chức năng chính

* Crawl dữ liệu sinh viên từ Backend API
* Lưu dữ liệu ra text file (`.txt`)
* Tiền xử lý dữ liệu bằng Pandas:

  * Chuẩn hóa dữ liệu
  * Xử lý giá trị thiếu
  * Chuẩn hóa tên cột
* Phân tích dữ liệu:

  * Phân bố điểm theo quê quán
  * So sánh điểm Toán / Tiếng Anh
* Trực quan hóa dữ liệu bằng biểu đồ
* Hiển thị dữ liệu dạng bảng

---

### 6.2 Cấu trúc thư mục FE3

```
desktop_app/
├── main.py
├── config.py
├── api/                # Gọi Backend API
├── crawler/            # Crawl dữ liệu
├── storage/            # Lưu & đọc text file
├── preprocessing/      # Pandas data cleaning & validation
├── analysis/           # Phân tích dữ liệu
├── visualization/      # Vẽ biểu đồ
├── ui/                 # PyQt5 UI
├── data/               # Text files
└── requirements.txt
```

---

### 6.3 Luồng xử lý dữ liệu FE3

1. Người dùng nhấn **Crawl Data**
2. Desktop App gọi API Backend
3. Dữ liệu JSON được lưu vào text file
4. Khi nhấn **Analyze Plot**:

   * Đọc dữ liệu từ file
   * Tiền xử lý bằng Pandas
   * Phân tích dữ liệu
   * Hiển thị bảng & biểu đồ

---

### 6.4 Chạy Desktop App

```bash
cd desktop_app
python main.py
```
