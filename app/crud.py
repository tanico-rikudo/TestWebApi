from sqlalchemy.orm import Session
from app import models, schemas
from app.logger import logger

def create_user(db: Session, user: schemas.UserCreate):
    logger.info(f"Called create_user with user {user}.")
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User {db_user.email} created.")
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    logger.info(f"Called get_users with skip={skip} and limit={limit}.")
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
