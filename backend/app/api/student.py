from fastapi import APIRouter, HTTPException
from app.services.student_service import StudentService
from app.models.student import StudentBase

router = APIRouter()
service = StudentService()


@router.get("/")
def get_all_students():
    return service.get_all_students()


@router.get("/{student_id}")
def get_student(student_id: str):
    student = service.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/")
def create_student(student: StudentBase):
    service.create_student(student.dict())
    return {"message": "Student created"}


@router.put("/{student_id}")
def update_student(student_id: str, student: StudentBase):
    service.update_student(student_id, student.dict())
    return {"message": "Student updated"}


@router.delete("/{student_id}")
def delete_student(student_id: str):
    service.delete_student(student_id)
    return {"message": "Student deleted"}
