from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from tags_docs import tags
from . import service, schemas, models

router = APIRouter()



@router.get("/", tags=[tags[1]], status_code=200,
            response_model=List[schemas.DieCutGetListSchema]
            )
async def get_diecut_list(db: Session = Depends(get_db)):
    return service.get_diecut_list(db)


@router.get("/{id}", tags=[tags[1]],
            description="Получить данные штампа по его cut_name",
            response_description='описание ответа',
            response_model=schemas.DieCutGetSinglSchema)
async def get_diecut_id(id: str,
                        db: Session = Depends(get_db)):
    return service.get_diecut_single(db=db, diecut_id=id.upper())


@router.delete("/{id}", tags=[tags[1]],
               description="Удаление штампа по его cut_name")
async def delete_diecut_id(id: str, db: Session = Depends(get_db)):
    return service.delete_diecut_single(db=db, diecut_id=id.upper())


@router.post("/", tags=[tags[1]],
             status_code=201,
             description="Создание штампа")
async def post_newdiecut(item: schemas.DieCutCreateSchema,
                         db: Session = Depends(get_db)):
    return service.create_diecut(db=db, item=item)


@router.patch("/{item_id}", tags=[tags[1]],
              status_code=200,
              description="Редактирование штампа по cut_name.")
async def update_item(item: schemas.DieCutSchema, item_id: str,
                      db: Session = Depends(get_db)):
    return service.update_diecut_single(db=db, item_id=item_id.upper(), item=item)


