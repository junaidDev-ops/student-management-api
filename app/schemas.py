from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length= 50)
    email: EmailStr
    age: int = Field(age=16, le=100)
    course: str = Field(min_length=2, max_length=50)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    course: str
    is_active: bool

    class Config:
        from_attributes = True

class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr | None = None
    age: int | None = Field(default= None, age=16, le=100)
    course: str | None = Field(default= None, min_length=2, max_length=50)