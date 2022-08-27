# API used --> FastApi(Web Framework)
# Importing Optional --> to make parameters optional

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# Initiating an instance of the fastApi 
app = FastAPI()

# Main data for operations
students = {
    1: {
        "name" : "john",
        "age" : 17,
        "class" : "12th"
    }
}
# amazon.com/create-user
# GET --> get an information
# POST --> create something new
# PUT --> Update
# DELETE --> Delete Something

@app.get("/")
def index():
    return {"name" : "first Data"}

# google.com/get-student/1

@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None, description = "The ID OF the student you want",gt = 0)):
    if student_id not in students:
        return {"Message": "Student doesn't exist"}
    else:
        print(student_id)
    print(students)
    return students[student_id]

# gt --> Greater than 
# lt --> less than
# ge --> Greater than or equal to
# le --> Lesser than or equal to

# google.com/results?search=Python

@app.get("/get-by-name/{student_id}")

#Optional--> We use Optional to make it Optional to be string
# Test --> is an Required Argument 
# Test --> We have to place a required argument before an optinal paramter

def get_student(*,name : Optional[str] = None,test:int,student_id):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data" : "Not Found"}

#-->Class made to set a required format of the input for a student
#-->Used in create_student function
class Student(BaseModel):
    name: str
    age: int
    year: str


#-->Class made to set a required format of the input for a student
#-->Used in update_student function
class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

@app.post("/create-student/{student_id}")
def create_student(student_id:int,student : Student):
    if student_id in students:
        return {"Error" : "ID Already exist"}
    
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exist"}

#-->Made to avoid the error of updating only one value
##-->By default others will set to null
#-->But now Will take the already set values(not nuLL)
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    del students[student_id]
    return {"Message" : "Student deleted succesfully"}
