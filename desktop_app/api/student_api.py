import requests

BASE_URL = "http://127.0.0.1:8000/students"


def get_all_students():
    res = requests.get(BASE_URL)
    res.raise_for_status()
    return res.json()


def create_student(data):
    res = requests.post(BASE_URL, json=data)
    res.raise_for_status()


def update_student(student_id, data):
    res = requests.put(f"{BASE_URL}/{student_id}", json=data)
    res.raise_for_status()


def delete_student(student_id):
    res = requests.delete(f"{BASE_URL}/{student_id}")
    res.raise_for_status()

def get_students_paged(page=1, page_size=10, keyword=None):
    params = {
        "page": page,
        "page_size": page_size
    }
    if keyword:
        params["keyword"] = keyword

    response = requests.get(f"{BASE_URL}/paged", params=params)
    response.raise_for_status()
    return response.json()
