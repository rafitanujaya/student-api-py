from flask import make_response, abort
from config import db
from src.models.student_model import Student, StudentSchema
from src.utils.randomNumber import random_id


def getAllStudent():
    student= Student.query.order_by(Student.name).all()
    print(student)

    studentSchema = StudentSchema(many=True)
    data = studentSchema.dump(student)
    print(data)
    return data


def getStudentById(Id):
    student = Student.query.filter(Student.id == Id).one_or_none()
    if student is not None:
        student_schema = StudentSchema()
        data = student_schema.dump(student)
        return data
    else:
        abort(404,  f"Student Not Found For ID :{Id}")


def addStudent(student):
    name = student.get("name")
    age = student.get("age")
    gender = student.get("gender")
    class_number = student.get("class_number")

    existing_student = (
        Student.query.filter(Student.name == name)
        .filter(Student.age == age)
        .filter(Student.gender == gender)
        .filter(Student.class_number == class_number)
        .one_or_none()
    )

    if existing_student is None:
        schema = StudentSchema()

        if gender.lower() not in {"l", "p"}:
            abort(400, "inputan umur harus l/p")
        new_Student = Student(
            id=random_id(length=4),
            name=name,
            age=age,
            gender=gender,
            class_number=class_number,
            created_at=db.func.now(),
        )

        db.session.add(new_Student)
        db.session.commit()

        data = schema.dump(new_Student)
        return data, 201

    else:
        abort(409, f"Milestone {name} {age} {gender} {class_number} exists already")


def updateStudent(Id, student):
    update_student = Student.query.filter(Student.id == Id).one_or_none()

    if update_student is None:
        abort(404, f"Student not found for id: {Id}")

    name = student.get("name")
    age = student.get("age")
    gender = student.get("gender")
    class_number = student.get("class_number")

    # Check for existing student with the same attributes
    existing_student = (
        Student.query.filter(Student.name == name)
        .filter(Student.age == age)
        .filter(Student.gender == gender)
        .filter(Student.class_number == class_number)
        .one_or_none()
    )
    
    if existing_student is not None and existing_student.id != Id:
        abort(409, f"Student {name} {age} {gender} exists already")

    # Update properties of update_student
    update_student.name = name
    update_student.age = age
    update_student.gender = gender
    update_student.class_number = class_number

    # Commit the changes
    db.session.commit()

    schema = StudentSchema()
    data = schema.dump(update_student)
    return data, 200


def deletedStudentById(Id):
    student = Student.query.filter(Student.id == Id).one_or_none()

    if student is not None:
        db.session.delete(student)
        db.session.commit()
        return make_response(f"student {Id} deleted")
    else:
        abort(f"student not found for id : {Id}")
