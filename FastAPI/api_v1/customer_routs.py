from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload
from core.utils import get_db
from tags_docs import tags
from typing import List, Any

router = APIRouter()

from auth import AuthHandler

from . import service, schemas, models

router = APIRouter()

auth_handler = AuthHandler()

#  /api/v1/customer
@router.get('/{id}',
            status_code=200,
            description="Получить данные заказчика",
            )
async def get_single_design(id: int, db: Session = Depends(get_db)):
    try:
        get_customer = db.query(models.Customer).filter(models.Customer.id == id).one()
        return jsonable_encoder(get_customer)
    except SQLAlchemyError as e:
        error = str(e._code_str)
    print(error)
    pass


@router.get("/", status_code=200,
            response_model=List[schemas.CustomerListSchema]
            )
async def get_diecut_list(db: Session = Depends(get_db)):
    return service.get_customer_list(db)


@router.post("/",
             status_code=201,
             description="Создание заказчика")
async def post_new_сustomer(item: schemas.Customer,
                           db: Session = Depends(get_db)):
    return service.create_customer(db=db, item=item)


@router.delete("/{id}",
               description="Удаление заказчика по ID")
async def delete_diecut_id(id: str, db: Session = Depends(get_db)):
    return service.delete_customer(db=db, id=id)


@router.patch("/{id}",
              status_code=200,
              description="Редактирование записи заказчика в БД по ID")
async def update_item(item: schemas.Customer, id: int,
                      db: Session = Depends(get_db)):
    return service.update_customer_single(db=db, id=id, item=item)
