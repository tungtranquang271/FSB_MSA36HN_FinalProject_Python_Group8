from app.repositories.student_repo import StudentRepository

class StudentService:

    def __init__(self):
        self.repo = StudentRepository()

    def get_all_students(self):
        return self.repo.find_all()

    def get_student(self, student_id: str):
        return self.repo.find_by_student_id(student_id)

    def create_student(self, data: dict):
        return self.repo.insert(data)

    def update_student(self, student_id: str, data: dict):
        return self.repo.update(student_id, data)

    def delete_student(self, student_id: str):
        return self.repo.delete(student_id)
