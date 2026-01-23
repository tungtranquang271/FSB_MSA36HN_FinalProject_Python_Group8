from app.core.database import student_collection


class StudentRepository:

    def find_all(self):
        return list(student_collection.find({}, {"_id": 0}))

    def find_all_paginated(
        self,
        page: int = 1,
        page_size: int = 10,
        keyword: str | None = None
    ):
        query = {}

        if keyword:
            query["$or"] = [
                {"student_id": {"$regex": keyword, "$options": "i"}},
                {"first_name": {"$regex": keyword, "$options": "i"}},
                {"last_name": {"$regex": keyword, "$options": "i"}},
                {"email": {"$regex": keyword, "$options": "i"}},
                {"hometown": {"$regex": keyword, "$options": "i"}},
            ]

        skip = (page - 1) * page_size

        cursor = (
            student_collection
            .find(query, {"_id": 0})
            .sort("student_id", 1)   
            .skip(skip)
            .limit(page_size)
        )

        total = student_collection.count_documents(query)

        return {
            "items": list(cursor),
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": (total + page_size - 1) // page_size
        }

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

    