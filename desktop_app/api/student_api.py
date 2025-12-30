import requests

BASE_URL = "http://127.0.0.1:8000"

def get_all_students():
    """
    Call backend API to get all students
    """
    response = requests.get(f"{BASE_URL}/students")
    response.raise_for_status()
    return response.json()
