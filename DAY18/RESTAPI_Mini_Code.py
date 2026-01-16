from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

## Data Model

class Students(BaseModel):
    name: str
    USN: int
    
students = []

## Create POST
@app.post("/students")
def create_student(obj: Students):
    students.append(obj)
    return {"message":"Student Enrollment is done","student":obj}

## Get data
@app.get("/students")
def get_students():
    return students

## Get single student
@app.get("/students/{index}")
def get_student(index: int):
    return students[index]

## update 
@app.put("/students/{index}")
def update_student(index: int,obj: Students):
    students[index] = obj
    return {"message":"Student updated","student": obj}

## Delete
@app.delete("/students/{index}")
def delete_student(index: int):
    deleted = students.pop(index)
    return {"message":"student deleted","student": deleted}