from app.core.database import student_collection
from datetime import datetime
import random

# Vietnamese names data
first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Võ", "Đặng", "Bùi", "Đỗ"]
last_names = ["Văn A", "Thị B", "Minh C", "Anh D", "Tùng E", "Lan F", "Hải G", "Mai H", "Long I", "Trang J"]
cities = ["Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Cần Thơ", "Hải Phòng", "Huế", "Nha Trang", "Vũng Tàu", "Quảng Ninh", "Bình Dương"]

# Generate 100 sample students
sample_students = []
for i in range(1, 101):
    student_id = f"SV{i:03d}"  # SV001, SV002, ..., SV100
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}{last_name.lower().replace(' ', '')}{i}@example.com"
    # Random birth date between 1995-2005
    year = random.randint(1995, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Avoid invalid dates
    date_of_birth = datetime(year, month, day)
    hometown = random.choice(cities)
    if hometown == "Hà Nội":
        math = round(random.uniform(8.0, 10.0), 1)
        literature = round(random.uniform(8.0, 10.0), 1)
        english = round(random.uniform(8.0, 10.0), 1)
    else:
        math = round(random.uniform(5.0, 8.0), 1)
        literature = round(random.uniform(5.0, 8.0), 1)
        english = round(random.uniform(5.0, 8.0), 1)

    student = {
        "student_id": student_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "date_of_birth": date_of_birth,
        "hometown": hometown,
        "math": math,
        "literature": literature,
        "english": english
    }
    sample_students.append(student)

try:
    # Clear existing data first
    student_collection.delete_many({})
    print("🗑️  Đã xóa dữ liệu cũ.")

    result = student_collection.insert_many(sample_students)
    print(f"✅ Đã thêm {len(result.inserted_ids)} học sinh mẫu vào database.")
    print(f"ID của tài liệu đầu tiên: {result.inserted_ids[0]}")
    print(f"ID của tài liệu cuối cùng: {result.inserted_ids[-1]}")
except Exception as e:
    print(f"❌ Lỗi khi thêm dữ liệu: {e}")