from pydantic import BaseModel
from typing import Optional
from datetime import date

class StudentBase(BaseModel):
    student_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    date_of_birth: Optional[date] = None
    hometown: Optional[str] = None
    math: Optional[float] = None
    literature: Optional[float] = None
    english: Optional[float] = None
