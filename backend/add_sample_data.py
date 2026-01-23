from app.core.database import student_collection
from datetime import datetime
import random

first_names = [
    "Nguyen", "Tran", "Le", "Pham", "Hoang",
    "Huynh", "Vo", "Dang", "Bui", "Do"
]

last_names = [
    "Van A", "Thi B", "Minh C", "Anh D", "Tung E",
    "Lan F", "Hai G", "Mai H", "Long I", "Trang J"
]

cities = [
    "Ha Noi", "Ho Chi Minh", "Da Nang", "Can Tho",
    "Hai Phong", "Hue", "Nha Trang", "Vung Tau",
    "Quang Ninh", "Binh Duong"
]

sample_students = []

TOTAL_RECORDS = 100
UNIQUE_IDS = 70        # 70 unique
DUPLICATE_RECORDS = 30 # 30 duplicate

# ----------------------
# 1. Generate 70 UNIQUE student_id
# ----------------------
student_ids = [f"SV{i:03d}" for i in range(1, UNIQUE_IDS + 1)]

# ----------------------
# 2. Add 30 DUPLICATE student_id
# ----------------------
student_ids += random.choices(student_ids, k=DUPLICATE_RECORDS)

# Shuffle to mix duplicates
random.shuffle(student_ids)

# ----------------------
# 3. Generate records
# ----------------------
for student_id in student_ids:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # 20% missing email
    email = (
        f"{first_name.lower()}{last_name.lower().replace(' ', '')}{random.randint(1,999)}@example.com"
        if random.random() > 0.2
        else None
    )

    # 15% missing date_of_birth
    if random.random() > 0.15:
        year = random.randint(1995, 2005)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date_of_birth = datetime(year, month, day)
    else:
        date_of_birth = None

    # 10% missing hometown
    hometown = random.choice(cities) if random.random() > 0.1 else None

    # Scores with missing values
    def random_score(min_val, max_val, missing_rate=0.2):
        return round(random.uniform(min_val, max_val), 1) if random.random() > missing_rate else None

    if hometown == "Ha Noi":
        math = random_score(8.0, 10.0)
        literature = random_score(8.0, 10.0)
        english = random_score(8.0, 10.0)
    else:
        math = random_score(5.0, 8.0)
        literature = random_score(5.0, 8.0)
        english = random_score(5.0, 8.0)

    student = {
        "student_id": student_id,   # 🔥 DUPLICATE HERE
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

# ----------------------
# 4. Insert to DB
# ----------------------
try:
    student_collection.delete_many({})
    print("🗑️  Old data removed.")

    result = student_collection.insert_many(sample_students)
    print(f"✅ Inserted {len(result.inserted_ids)} EXTREMELY DIRTY records.")

except Exception as e:
    print(f"❌ Insert error: {e}")
