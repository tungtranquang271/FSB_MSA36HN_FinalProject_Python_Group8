from app.core.database import student_collection

class StudentRepository:

    def find_all(self):
        return list(student_collection.find({}, {"_id": 0}))

    def find_by_student_id(self, student_id: str):
        return student_collection.find_one(
            {"student_id": student_id},
            {"_id": 0}
        )

    def insert(self, data: dict):
        return student_collection.insert_one(data)

    def update(self, student_id: str, data: dict):
        return student_collection.update_one(
            {"student_id": student_id},
            {"$set": data}
        )

    def delete(self, student_id: str):
        return student_collection.delete_one(
            {"student_id": student_id}
        )
