from api.student_api import get_all_students
from storage.file_storage import save_to_text_file

RAW_FILE = "students_raw.txt"


def crawl_students():
    """
    Crawl student data and save RAW data only
    """
    raw_students = get_all_students()
    save_to_text_file(raw_students, RAW_FILE)
    
    return raw_students
