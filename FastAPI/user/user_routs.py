from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from core.utils import get_db

router = APIRouter()

from auth import AuthHandler

from . import service, schemas, models

router = APIRouter()

auth_handler = AuthHandler()

db: Session = Depends(get_db)


@router.get("/protected")
async def protected(username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    print(username)
    return jsonable_encoder(service.test_jwt(db=db))


@router.post('/login',
             status_code=200,
             description="Авторизация пользователя")
async def get_user(item: schemas.AuthUserSchema, db: Session = Depends(get_db)):
    data = schemas.AuthUserSchema(**item.dict(exclude_unset=True))
    data_mod = models.User(**data.dict())
    # # # берем данные пользователя с сервера по email 
    get_user = db.query(models.User).options(joinedload('role_user')).filter(models.User.email == data_mod.email).one()
    print('get_user: -> ', jsonable_encoder(get_user))
    if get_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    verify_password = auth_handler.verify_password(plain_password=data_mod.password, hashed_password=get_user.password)
    """verify_password - проверка пароля"""

    if verify_password:
        get_user.token = auth_handler.encode_token(user_id=get_user.name)
        verifi_token = auth_handler.decode_token(token=get_user.token)
        print('verifi_token: -> ', verifi_token)
        return schemas.LoginUserSchema(**(jsonable_encoder(get_user)))
    raise HTTPException(status_code=400, detail='Password isn`t correct')


@router.post('/me',
             status_code=200,
             description="Возвращает имя авторизованного пользователя")
async def read_users_me(item: schemas.Token, db: Session = Depends(get_db)):
    verifi_token = auth_handler.decode_token(token=item.token)
    if verifi_token:
        get_user = db.query(models.User).options(joinedload('role_user')).filter(models.User.name == verifi_token).one()
        return schemas.MeSchema(**(jsonable_encoder(get_user)))
    raise HTTPException(status_code=400, detail='Token isn`t correct')


@router.post('/register',
             status_code=201,
             description="Регистрация пользователя")
async def register(item: schemas.RegUserSchema, db: Session = Depends(get_db)):
    ### прогоняем полученные данные через схему 
    data = schemas.RegUserSchema(**item.dict(exclude_unset=True))
    data_mod = models.User(**data.dict())
    print('data_mod -->>  ', data_mod)
    ### хешируем пороль и записываем его вместо входящего
    hashed_password = auth_handler.get_password_hash(item.password)
    data_mod.password = hashed_password
    item_check = db.query(models.User).filter(models.User.email == data.email).first()
    if item_check is None:
        db.add(data_mod)
        db.commit()
        db.refresh(data_mod)
        get_user = db.query(models.User).options(joinedload('role_user')).filter(
            models.User.email == data_mod.email).one()
        print('type(get_user): ', type(get_user))
        print('get_user : ', get_user)
        print(schemas.MeSchema(**(jsonable_encoder(get_user))))
        return schemas.MeSchema(**(jsonable_encoder(get_user)))
    raise HTTPException(status_code=400, detail='Username is taken')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # get_user = db.query(models.User).filter(models.User.name == data_mod.name).first()
    # ### get_user = db.query(models.Child).all()
    # print('type(get_user): ', type(get_user))
    # print('(jsonable_encoder(get_user) : ', jsonable_encoder(get_user))
    # print(schemas.GetUserSchema(**(jsonable_encoder(get_user))))
    # print('jsonable_encoder(get_user) -->>> ', f"    {result_users.__dict__}")
    # result_users = db.query(models.Role).options(joinedload('users_role')).first()
    # 
    # get_users = db.query(models.User).options(joinedload('role_user')).filter(models.User.name == 'test_reg').one()
    # # for get_user in get_users:
    # print('jsonable_encoder(get_user) -->>> ', f"    {jsonable_encoder(get_users)}")
    # # получить дизайн ID = 1 и присоеденить таблицу частей с частями где models.Part.design_id == 1
    # print("//-//-" * 20)
    # get_gesign = db.query(Design).options(joinedload('parts')).filter(Design.design_id == 1).all()
    # print('jsonable_encoder(get_gesign) -->>> ', f"    {jsonable_encoder(get_gesign)}")
    # 
    # return jsonable_encoder(get_users)
    # print("//-//-"*30)
    # print('{get_user.role_user.role} - {get_user.role_user.description} -->>> ', f"        {get_user.role_user.role} - {get_user.role_user.description}")
    # 
    # print(get_user.__dict__)
    # print(get_user.role_user.__dict__)
    # 
    # print("//-//-"*30)
    # print("Результат Роли:")
    # get_roles = db.query(models.Role).options(joinedload('users_role')).all()
    # for get_role in get_roles:
    #     print('{get_role.role} - {get_role.description} -->>> ', f'    {get_role.role} - {get_role.description}')
    #     for get_user in get_role.users_role:
    #         print('{get_user.name} -->>> ', f"        {get_user.name}")
    # return 

# users = service.get_user_list(db)
# if any(x['username'] == item.username for x in users):
#     raise HTTPException(status_code=400, detail='Username is taken')
# hashed_password = auth_handler.get_password_hash(item.password)
# item.password = hashed_password
# db.add(diecut)
# db.commit()
# db.refresh(diecut)
# return diecut
# users.append({
#     'email': item.email,
#     'password': hashed_password
# })
# return

# 
# @router.post("/", tags=[tags[1]],
#              status_code=201,
#              description="Создание штампа")
# async def post_newdiecut(item: schemas.DieCutCreateSchema,
#                          db: Session = Depends(get_db)):
#     return create_diecut(db=db, item=item)
# 
# 
# def create_diecut(db: Session, item: schemas.DieCutCreateSchema):
#     diecut = models.DieCut(**item.dict())
#     print(diecut.cut_name)
#     item = db.query(models.DieCut).filter(models.DieCut.cut_name == diecut.cut_name).first()
#     if item is None:
#         db.add(diecut)
#         db.commit()
#         db.refresh(diecut)
#         return diecut
#     return {"msg": "Такой штамп существует"}
