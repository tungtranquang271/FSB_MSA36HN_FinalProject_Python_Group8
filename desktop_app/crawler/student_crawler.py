from api.student_api import get_all_students

def crawl_students():
    """
    Crawl student data from backend API
    """
    students = get_all_students()
    return students
