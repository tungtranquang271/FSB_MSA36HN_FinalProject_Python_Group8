from api.student_api import get_all_students
from preprocessing.data_cleaner import clean_student_data

def crawl_students():
    """
    Crawl, clean and sort student data
    """
    raw_students = get_all_students()

    # 🔹 Clean data (duplicate, null handling)
    clean_df = clean_student_data(raw_students)

    # 🔹 Sort by student_id (ổn định)
    if "student_id" in clean_df.columns:
        clean_df = clean_df.sort_values("student_id")

    # 🔹 Convert back to list of dict
    return clean_df.to_dict(orient="records")
