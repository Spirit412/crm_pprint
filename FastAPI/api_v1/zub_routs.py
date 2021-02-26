from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from tags_docs import tags
from . import service, schemas, models

router = APIRouter()


# ZUB
@router.get("/{id}", tags=[tags[2]], response_model=schemas.ZubSchema)
async def get_zub_id(id: str, db: Session = Depends(get_db)):
    return service.get_zub_single(db=db, zub_id=id)


@router.get("/", tags=[tags[2]], response_model=List[schemas.ZubSchema])
async def get_zub_list(db: Session = Depends(get_db)):

    return service.get_zub_list(db)
