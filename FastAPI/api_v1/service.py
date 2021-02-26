import sys

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Body, FastAPI, status
from sqlalchemy import or_, func
from sqlalchemy.orm import Session
from . import models, schemas

from datetime import *


def get_diecut_list(db: Session):
    stored_list = db.query(models.DieCut).all()
    return stored_list


def get_diecut_single(db: Session, diecut_id: str):
    get_data = db.query(models.DieCut).filter(func.lower(models.DieCut.cut_name) == func.lower(diecut_id)).first()
    if get_data is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"msg": "Не найдено"})
    return get_data


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


def update_diecut_single(db: Session, item_id: str, item):
    # RESPONSE
    # данные из запроса прогоняем через схему: Схема принимает распакованный DICT.
    # Отключаем значения по умолчанию в схеме: exclude_unset=True
    update_data = schemas.DieCutSchema(**item.dict(exclude_unset=True))
    print('\n тип  ==>>  update_data ', type(update_data))
    print('\n данные из запроса прогоняем через схему ==>>  update_data ', update_data)

    # далее прогоняем через модель DB. Модель принимает РАСПАКОВАННЫЙ DICT
    update_data_mod = models.DieCut(**update_data.dict())
    print('\n далее прогоняем через модель Бд ==>>  update_data_mod ', update_data_mod)
    print('\n DICT ==>>  jsonable_encoder(update_data_mod) ', jsonable_encoder(update_data_mod))

    # STORE
    # выбираем запись из  БД по фильтру id из URL. Записываем как DICT
    stored_item_data = db.query(models.DieCut).filter(models.DieCut.cut_name == item_id.upper()).first()
    print('\n выбираем запись в БД ==>>  stored_item_data ', stored_item_data)
    # запись из БД распаковываем и прогоняем через схему
    stored_item_model = schemas.DieCutSchema(**(jsonable_encoder(stored_item_data)))
    print('\n запись из БД распаковываем и прогоняем через схему stored_item_model ==>>  ', stored_item_model)
    # //////////////////////
    #
    updated_item = stored_item_model.copy(update=update_data)
    print('\n ==>>  updated_item :', updated_item)
    db.query(models.DieCut).filter(models.DieCut.cut_name == item_id.upper()).update(updated_item)
    # /////////////////////
    db.commit()
    # возвращаем изменённую запись
    return jsonable_encoder(db.query(models.DieCut).filter(models.DieCut.cut_name == update_data_mod.cut_name).first())


def get_zub_single(db: Session, zub_id: str):
    return db.query(models.Zub).filter(models.Zub.zub_num == zub_id).first()


def get_zub_list(db: Session):
    return db.query(models.Zub).all()
