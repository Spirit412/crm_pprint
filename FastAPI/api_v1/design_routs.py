from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from core.utils import get_db
from tags_docs import tags
router = APIRouter()

from auth import AuthHandler

from . import service, schemas, models

router = APIRouter()

auth_handler = AuthHandler()


@router.get('/{design_id}',
            status_code=200,
            description="Получить дизайн",
            response_model=schemas.Design,
            )
async def get_single_design(design_id: str, db: Session = Depends(get_db)):
    """
    
    :param design_id: id дизайна который требуется получить 
    :param db: midlware работы с БД
    :return: json данные одного дизайна
    """
    # get_gesign = db.query(models.Design).options(joinedload('parts')).filter(models.Design.design_num == design_id).all()
    # print('jsonable_encoder(get_gesign) -->>> ', f"    {jsonable_encoder(get_gesign)}")
    # print('auth -->>  ', "auth")
    # return jsonable_encoder(get_gesign)
    return service.get_single_design(db=db, design_id=design_id)
