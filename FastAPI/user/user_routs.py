from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db

router = APIRouter()


@router.get("/")
def user(db: Session = Depends(get_db)):
    print(db)
    return {"msg": "test user content"}
