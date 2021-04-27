from typing import List, Any

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from core.utils import get_db
from tags_docs import tags
from . import service, schemas, models
from fastapi.encoders import jsonable_encoder

from fastapi import FastAPI, Response

router = APIRouter()


# ZUB
@router.get("/{id}", response_model=schemas.ZubSchema)
async def get_zub_id(id: str, db: Session = Depends(get_db)):
    return service.get_zub_single(db=db, zub_id=id)


@router.get("/", response_model=List[schemas.ZubSchema])
async def get_zub_list(db: Session = Depends(get_db)):
    isJson = jsonable_encoder(service.get_zub_list(db))
    return isJson
