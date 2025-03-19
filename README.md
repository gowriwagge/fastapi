# FastAPI Backend Project

This is a backend project built using **FastAPI** for developing RESTful APIs. It includes features such as user authentication, database management using SQLAlchemy, and password hashing with secure storage.

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
