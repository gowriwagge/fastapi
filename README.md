# FastAPI Backend Project

This is a backend project built using **FastAPI** for developing RESTful APIs. It includes features such as user authentication, database management using SQLAlchemy, and password hashing.

## Features
- User registration and login
- Password hashing and verification
- CRUD operations for user data
- Database integration using SQLAlchemy
- API routing with FastAPI
- Environment management using `.env`

## Project Structure
```bash
backend/
├── crud/              # CRUD operations
├── models/            # Database models
├── routes/            # API routes
├── schemas/           # Pydantic models for data validation
├── utils/             # Utility functions (e.g., hashing passwords)
├── env/               # Virtual environment
├── .env               # Environment variables
├── index.py           # Main entry point
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
# FastAPI Project

## Prerequisites
- Python 3.10+
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic
- bcrypt

## Installation

### Clone the repository:
```bash
git clone https://github.com/gowriwagge/fastapi.git
cd fastapi/backend
## Running the Server

### Start the server using Uvicorn:
```bash
uvicorn index:app --reload

##Access the API at:
http://127.0.0.1:8000
