from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserSchema, UpdateUserSchema
from database import get_db
import crud.user as crud_user

router = APIRouter()  # Ensure you're using `router` here, not `user`

@router.post("/", status_code=201)
async def create_user(new_user: UserSchema, db: Session = Depends(get_db)):
    """Create a new user."""
    response = crud_user.create_user(db, new_user)
    if "id" in response:
        return {"message": response["message"], "id": response["id"]}
    raise HTTPException(status_code=400, detail="User creation failed")

@router.get("/{id}")
async def get_user(id: int, db: Session = Depends(get_db)):
    """Get user by ID."""
    user_data = crud_user.get_user(db, id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data

@router.get("/search/")
async def get_users_by_name(name: str, db: Session = Depends(get_db)):
    """Search users by name."""
    users_data = crud_user.get_users_by_name(db, name)
    if not users_data:
        raise HTTPException(status_code=404, detail="No users found with the given name")
    return users_data

@router.put("/{id}")
async def update_user(id: int, updated_user: UpdateUserSchema, db: Session = Depends(get_db)):
    """Update user details."""
    success = crud_user.update_user(db, id, updated_user)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    """Delete user by ID."""
    success = crud_user.delete_user(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
