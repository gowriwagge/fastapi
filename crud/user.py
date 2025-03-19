from sqlalchemy.orm import Session
from sqlalchemy.sql import select, insert, update, delete
from models.user import users  # Corrected relative import
from schemas.user import UserSchema, UpdateUserSchema  # Corrected relative import
from utils.auth import hash_password, verify_password  # Corrected relative import

def create_user(db: Session, new_user: UserSchema):
    """Creates a new user in the database with a hashed password."""
    hashed_password = hash_password(new_user.password)  # Hash password
    user_data = new_user.dict(exclude_unset=True)
    user_data["password"] = hashed_password  # Store hashed password

    query = insert(users).values(**user_data)
    result = db.execute(query)
    db.commit()  # Commit after insertion
    
    # Retrieve the created user (optional, return user ID or full user)
    user_id = result.inserted_primary_key[0]  # This is the primary key of the inserted row
    return {"message": "User created successfully", "id": user_id}

def get_user(db: Session, user_id: int):
    """Fetches a user by ID."""
    query = select(users).where(users.c.id == user_id)
    result = db.execute(query).fetchone()
    return dict(result._mapping) if result else None

def get_users_by_name(db: Session, name: str):
    """Fetches users by name."""
    query = select(users).where(users.c.name.ilike(f"%{name}%"))  # Use ilike for case-insensitive search
    result = db.execute(query).fetchall()
    return [dict(zip(users.columns.keys(), row)) for row in result] if result else None

def update_user(db: Session, user_id: int, updated_user: UpdateUserSchema):
    """Updates user details."""
    # Check if user exists before updating
    existing_user = get_user(db, user_id)
    if not existing_user:
        return None  # No user found to update

    query = update(users).where(users.c.id == user_id).values(**updated_user.dict(exclude_unset=True))
    result = db.execute(query)
    db.commit()
    
    # Check if any rows were affected (i.e., updated)
    return result.rowcount > 0  # True if update was successful, otherwise False

def delete_user(db: Session, user_id: int):
    """Deletes a user from the database."""
    # Check if user exists before deleting
    existing_user = get_user(db, user_id)
    if not existing_user:
        return False  # No user found to delete
    
    query = delete(users).where(users.c.id == user_id)
    result = db.execute(query)
    db.commit()
    
    # Check if any rows were affected (i.e., deleted)
    return result.rowcount > 0  # True if delete was successful, otherwise False
