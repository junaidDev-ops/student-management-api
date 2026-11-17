from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session 
from sqlalchemy.exc import IntegrityError

from .database import engine, Base, get_db
from . import models, schemas


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management Api")


@app.get("/")
def home():
    return {"message": "Student Management Api is running"}




@app.post("/students", response_model=schemas.StudentResponse)
def add_student(
    student: schemas.StudentCreate,
    db: session = Depends(get_db)
):
    
    # email check

    existing_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code= 400,
            detail="Email already registered"
        )

    
    # student object 

    new_student = models.Student(
        name=student.name,
        email=student.email,
        age=student.age,
        course=student.course
    )

    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Could not create student"
        )
    return new_student





@app.get("/students", response_model=list[schemas.StudentResponse])
def get_students(db:Session = Depends(get_db)):

    students = db.query(models.Student).all()

    return students




@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_students(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student



@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student_data: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

   student = db.query(models.Student).filter(
    models.Student.id == student_id
   ).first()

   if student is None:
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

   existing_email = db.query(models.Student).filter(
    models.Student.email == student_data.email,
    models.Student.id != student_id
   ).first()

   if existing_email:
    raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )

   student.name = student_data.name
   student.email = student_data.email
   student.age = student_data.age
   student.course = student_data.course

   db.commit()
   db.refresh(student)

   return student



@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(
    models.Student.id == student_id
).first()

    if student is None:
        raise HTTPException(

            status_code=404,
            detail="Student not found"
            )

    db.delete(student)
    db.commit()
        
    return{
        "message": "Student deleted successfully"
    }



@app.patch("/students/{student_id}", response_model=schemas.StudentResponse)
def patch_student(
    student_id:int,
    student_data: schemas.StudentUpdate,
    db: session = Depends(get_db)
):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = student_data.model_dump(exclude_unset=True)

    if "email" in update_data:
        existing_email = db.query(models.Student).filter(
            models.Student.email == update_data["email"],
            models.Student.id != student_id
        ).first()


        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student

    



 



