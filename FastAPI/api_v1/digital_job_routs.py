from typing import List

from fastapi import APIRouter, Depends
from fastapi import status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload, lazyload, subqueryload
from sqlalchemy import exc
from core.utils import get_db
from tags_docs import tags

from pydantic import ValidationError

router = APIRouter()
from auth import AuthHandler

from . import service, schemas, models

router = APIRouter()

auth_handler = AuthHandler()


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            description="Получить данные цифрового заказа по его номеру",
            )
async def get_single_digitaljob(id: str, db: Session = Depends(get_db)):
    """
    :param id: id  цифрового заказа
    :param db: 
    :return: json данные одного цифрового заказа
    """
    try:
        get_gesign = db.query(models.DigitalJobPrint).options(
            joinedload('frames'),
            # joinedload('customer') name backref
            joinedload('customer')) \
            .filter(models.DigitalJobPrint.digitaljob_num == id).one()
        return jsonable_encoder(get_gesign)
    except SQLAlchemyError as e:
        error = str(e._code_str)
    print(error)
    pass


data_in = {
    "diecut_cut_name": "A1001",
    "bleed": "1.5",
    "razmeshenie": "h",
    "digitaljob_num": "05 0001",
    "customer_id": 8,
    "color_print": "cmyk",
    "descript": "описание",
    "frames": [
        {
            "frame_num": 1,
            "descript": "описание фрейма 1",
            "rows": [
                {
                    "descript": "описание 1 строки, фрейм #1",
                    "design_url": "\\\\TS\\Obmen\\190001__ED.pdf",
                    "row_number": 1,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 2 строки, фрейм #1",
                    "design_url": "\\\\TS\\Obmen\\190001__ED.pdf",
                    "row_number": 2,
                    "design_angle_rotate": 0
                }
            ]
        },
        {
            "frame_num": 2,
            "descript": "описание фрейма 2",
            "rows": [
                {
                    "descript": "описание 1 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200001__ED.pdf",
                    "row_number": 1,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 2 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200002__ED.pdf",
                    "row_number": 2,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 3 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200003__ED.pdf",
                    "row_number": 3,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 4 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200004__ED.pdf",
                    "row_number": 4,
                    "design_angle_rotate": 0
                }
            ]
        }
    ]
}


@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.DigitalJobTable],
            description="Получить список цифровых заказов")
async def get_all_djob(db: Session = Depends(get_db)):
    try:
        get_gesign = db.query(models.DigitalJobPrint).options(
            lazyload('frames'),
            # joinedload('customer') name backref
            joinedload('customer')) \
            .all()
        return jsonable_encoder(get_gesign)
    except SQLAlchemyError as e:
        error = str(e._code_str)
    print(error)
    pass


@router.post("/",
             status_code=status.HTTP_201_CREATED,
             description='Добавление цифрового заказа')
async def create_djob(data_input: schemas.DigitalJobPrint, db: Session = Depends(get_db)):
    data_input: dict = data_input.dict(exclude_unset=True)
    digitaljob_num: str = data_input['digitaljob_num']



    try:
        data_db = db.query(models.DigitalJobPrint.digitaljob_num).filter(
            models.DigitalJobPrint.digitaljob_num == digitaljob_num).first()
    except exc.SQLAlchemyError as e:
        return {"msg DB": f"{e}"}

    if data_db is None:

        frames_in_djob = []
        data_djob = data_input.copy()
        for data_frame_num in range(len(data_input['frames'])):  # каждый фрейм
            rows_in_frame = []

            for row_num_in_frame in range(len(data_input['frames'][data_frame_num]['rows'])):  # каждая строка в фрейме.
                data_row = data_input['frames'][data_frame_num]['rows'][row_num_in_frame]  # данные строки инпута
                data_row_mod = models.RowFrame(**data_row)  # данные строки инпута помещаем в модель
                rows_in_frame.append(data_row_mod)  # модель строки помещаем в список
            data_frame = data_input['frames'][data_frame_num]  # данные фрейма из инпута
            data_frame['rows'] = [*rows_in_frame]
            data_frame_mod = models.Frame(**data_frame)
            frames_in_djob.append(data_frame_mod)
        data_djob['frames'] = [*frames_in_djob]
        data_djob_mod = models.DigitalJobPrint(**data_djob)
        db.add(data_djob_mod)
        db.commit()
        db.refresh(data_djob_mod)
        # получим данные записи из БД
        data_db = db.query(models.DigitalJobPrint).filter(
            models.DigitalJobPrint.digitaljob_num == digitaljob_num).first()
        return schemas.DigitalJobPrint(**(jsonable_encoder(data_db)))

    else:
        return {"msg": "Такой DJOB существует"}
