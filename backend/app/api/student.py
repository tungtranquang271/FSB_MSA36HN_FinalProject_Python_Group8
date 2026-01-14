from fastapi import APIRouter
from app.services.student_service import StudentService
from app.models.student import StudentBase

router = APIRouter()
service = StudentService()


@router.get("/")
def get_all_students():
    return service.get_all_students()


@router.get("/{student_id}")
def get_student(student_id: str):
    return service.get_student(student_id)


@router.post("/")
def create_student(student: StudentBase):
    service.create_student(student.dict())
    return {"message": "Student created successfully"}


@router.put("/{student_id}")
def update_student(student_id: str, student: StudentBase):
    data = student.dict(exclude={"student_id"})
    service.update_student(student_id, data)
    return {"message": "Student updated successfully"}


@router.delete("/{student_id}")
def delete_student(student_id: str):
    service.delete_student(student_id)
    return {"message": "Student deleted successfully"}
