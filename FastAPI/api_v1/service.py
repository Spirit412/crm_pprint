import sys

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Body, FastAPI, status
from sqlalchemy import or_, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload
from . import models, schemas

from pydantic import BaseModel, ValidationError

from loguru import logger

fmt = "<green>{time}</green> - {name} - {level} - {message}"
logger.add(sys.stderr, format=fmt, filter="my_module", level="INFO", backtrace=True,
           diagnose=True, colorize=True)

from datetime import *


def get_diecut_list(db: Session):
    stored_list = db.query(models.DieCut).all()
    return stored_list


def get_diecut_single(db: Session, diecut_id: str):
    get_data = db.query(models.DieCut).filter(func.lower(models.DieCut.cut_name) == func.lower(diecut_id)).first()
    if get_data is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"msg": "Не найдено"})
    return get_data


def get_single_design(db: Session, design_id: str):
    get_gesign = db.query(models.Design).options(joinedload('parts')).filter(
        models.Design.design_num == design_id).first()
    if get_gesign is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"msg": "Не найдено"})
    return get_gesign


def delete_diecut_single(db: Session, diecut_id: str):
    item = db.query(models.DieCut).filter(models.DieCut.cut_name == diecut_id.upper()).first()
    if item is None:
        return {"msg": "Нет такого штампа"}
    db.delete(item)
    db.commit()
    return item


def create_diecut(db: Session, item: schemas.DieCutCreateSchema):
    diecut = models.DieCut(**item.dict())
    print(diecut.cut_name)
    item = db.query(models.DieCut).filter(models.DieCut.cut_name == diecut.cut_name).first()
    if item is None:
        db.add(diecut)
        db.commit()
        db.refresh(diecut)
        return diecut
    return {"msg": "Такой штамп существует"}




def delete_customer(db: Session, id: int):
    item = db.query(models.Customer).filter(models.Customer.id == id).first()
    if item is None:
        return {"msg": "Нет такого заказчика"}
    db.delete(item)
    db.commit()
    return item


def create_customer(db: Session, item: schemas.Customer):
    customer = models.Customer(**item.dict())
    item = db.query(models.Customer).filter(models.Customer.name == customer.name).first()
    if item is None:
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer
    return {"msg": "Такое имя заказчика есть в базе"}


def get_customer_list(db: Session):
    stored_list = db.query(models.Customer).all()
    return stored_list


def update_diecut_single(db: Session, item_id: str, item):
    ''' RESPONSE
    данные из запроса прогоняем через схему: Схема принимает распакованный DICT.
    Отключаем значения по умолчанию в схеме: exclude_unset=True'''
    update_data = schemas.DieCutSchema(**item.dict(exclude_unset=True))
    logger.info('\n тип  ==>>  update_data ' + f"{type(update_data)}")
    logger.info('\n данные из запроса прогоняем через схему ==>>  update_data ' + f"{update_data}")

    # далее прогоняем через модель DB. Модель принимает РАСПАКОВАННЫЙ DICT
    update_data_mod = models.DieCut(**update_data.dict())
    logger.info('\n далее прогоняем через модель Бд ==>>  update_data_mod ' + f"{update_data_mod}")

    # STORE
    # выбираем запись из  БД по фильтру id из URL. Записываем как DICT

    try:
        stored_item_data = db.query(models.DieCut).filter(models.DieCut.cut_name == item_id.upper()).one()
    except ValidationError as e:
        logger.error('pydantic ValidationError: ' + f"{e.json()}")

    logger.info('\n выбираем запись в БД ==>>  stored_item_data ' + f"{stored_item_data}")
    # запись из БД распаковываем и прогоняем через схему
    stored_item_model = schemas.DieCutSchema(**(jsonable_encoder(stored_item_data)))
    logger.info('\n запись из БД распаковываем и прогоняем через схему  ==>>  ' + f"{stored_item_model}")
    logger.info('\n update_data_mod в DICT ==>> ' + f"{jsonable_encoder(update_data_mod)}")
    # //////////////////////
    #
    try:
        updated_item = stored_item_model.copy(update=jsonable_encoder(update_data_mod))
    except ValidationError as e:
        logger.error('pydantic ValidationError: ' + f"{e.json()}")

    logger.info('\n ==>>  updated_item :', updated_item)
    db.query(models.DieCut).filter(models.DieCut.cut_name == item_id.upper()).update(updated_item)
    # /////////////////////
    db.commit()
    # возвращаем изменённую запись
    return jsonable_encoder(db.query(models.DieCut).filter(models.DieCut.cut_name == update_data_mod.cut_name).first())


def update_customer_single(db: Session, id: int, item):
    update_data = schemas.Customer(**item.dict(exclude_unset=True))
    update_data_mod = models.Customer(**update_data.dict())
    try:
        stored_item_data = db.query(models.Customer).filter(models.Customer.id == id).one()
    except ValidationError as e:
        logger.error('pydantic ValidationError: ' + f"{e.json()}")
        return e
    stored_item_model = schemas.Customer(**(jsonable_encoder(stored_item_data)))
    try:
        updated_item = stored_item_model.copy(update=jsonable_encoder(update_data_mod))
    except ValidationError as e:
        logger.error('pydantic ValidationError: ' + f"{e.json()}")
        return e
    db.query(models.Customer).filter(models.Customer.id == id).update(updated_item)
    db.commit()
    return jsonable_encoder(db.query(models.Customer).filter(models.Customer.id == id).first())


def get_zub_single(db: Session, zub_id: str):
    return db.query(models.Zub).filter(models.Zub.zub_num == zub_id).first()


def get_zub_list(db: Session):
    return db.query(models.Zub).all()
