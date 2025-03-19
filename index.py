from fastapi import FastAPI
from routes.user import router  # Correct import for the router object

app = FastAPI()

# Include user routes with prefix and tags for better organization
app.include_router(router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    """Home route that returns a simple welcome message."""
    return {"message": "Welcome to FastAPI Backend!"}
