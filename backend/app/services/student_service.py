from app.repositories.student_repo import StudentRepository
from fastapi import HTTPException


class StudentService:

    def __init__(self):
        self.repo = StudentRepository()

    def get_all_students(self):
        return self.repo.find_all()

    def get_student(self, student_id: str):
        student = self.repo.find_by_student_id(student_id)
        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )
        return student

    def create_student(self, data: dict):
        existing = self.repo.find_by_student_id(data.get("student_id"))
        if existing:
            raise HTTPException(
                status_code=400,
                detail="Student with this student_id already exists"
            )

        return self.repo.insert(data)

    def update_student(self, student_id: str, data: dict):
        existing = self.repo.find_by_student_id(student_id)
        if not existing:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        clean_data = {k: v for k, v in data.items() if v is not None}

        if not clean_data:
            raise HTTPException(
                status_code=400,
                detail="No valid fields to update"
            )

        result = self.repo.update(student_id, clean_data)

        if result.modified_count == 0:
            return {"message": "No changes detected"}

        return {"message": "Student updated successfully"}

    def delete_student(self, student_id: str):
        result = self.repo.delete(student_id)

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {"message": "Student deleted successfully"}
