
# Student Management API

This is a student management project I built using Python and FastAPI. The main purpose of this project is to manage student records through API endpoints.

I used SQLite to store student data and SQLAlchemy to interact with the database. FastAPI handles the API requests, while Pydantic is used to validate the data.

## What can this API do?

- Add a new student
- View all students
- Find a student using their ID
- Update student information
- Update only selected student fields
- Delete a student
- Prevent duplicate email addresses
- Validate student information
- Handle errors when a student is not found

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Project Structure

```text
Student Managment Api/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd Student-Managment-Api
```

**3. Install the required packages**

```bash
python -m pip install -r requirements.txt
```

**4. Start the server**

```bash
python -m uvicorn app.main:app --reload
```

The API will run at:

`http://127.0.0.1:8000`

## API Documentation

I used FastAPI's Swagger UI to test the endpoints.

Open this link after starting the server:

`http://127.0.0.1:8000/docs`

## Available API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students` | Add a student |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| PATCH | `/students/{student_id}` | Update selected fields |
| DELETE | `/students/{student_id}` | Delete a student |

## Screenshots

Screenshots of the API and its responses are available in the `screenshots` folder.

## Database

The project uses SQLite to save student records. The database is created automatically when the application starts.

## What I Learned

While building this project, I got practical experience with creating REST APIs, working with databases, handling HTTP requests, validating input data, and implementing CRUD operations.

## Author

Junaid Amanat
