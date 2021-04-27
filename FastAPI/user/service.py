from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from core.utils import get_db
from . import models, schemas

db: Session = Depends(get_db)


def get_user_list(db: Session):
    stored_list = db.query(models.User).all()
    return stored_list


def reg_user(db: Session, item: schemas.RegUserSchema):
    reguser = models.User(**item.dict())
    print(reguser.email, reguser.username, reguser.password, )
    item = db.query(models.User).filter(models.User.username == reguser.username).first()
    if item is None:
        db.add(reguser)
        db.commit()
        db.refresh(reguser)
        return reguser
    return {"msg": "Такой штамп существует"}


def test_jwt(db: Session):
    return db.query(models.User).all()
