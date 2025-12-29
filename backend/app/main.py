from fastapi import FastAPI
from app.api.student import router as student_router

app = FastAPI(title="Student Management API")

app.include_router(student_router)
