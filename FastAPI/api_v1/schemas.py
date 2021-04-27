from pydantic import condecimal, BaseModel, ValidationError, Field, ValidationError, validator
from typing import List, Optional, Dict
from datetime import datetime
from uuid import UUID


# добавим к BaseModel конфиг orm_mode = True что бы в каждом классе не прописывать
class BaseModel(BaseModel):
    class Config:
        orm_mode = True


class ZubSchema(BaseModel):
    zub_num: int
    hprint: condecimal(max_digits=10, decimal_places=4)
    hpolimer: condecimal(max_digits=10, decimal_places=4)
    hpolimer_17: condecimal(max_digits=10, decimal_places=4)
    version_uuid: str = None
    # '''столбец версии записи'''
    # created_on: datetime = Field(default_factory=datetime.utcnow)
    # updated_on: datetime = Field(default_factory=datetime.utcnow)


class DieCutSchema(BaseModel):
    cut_name: str = Field(..., example='Ex_cut')

    @validator('cut_name')
    def cut_name_must_upper(cls, v):
        if v.isupper():
            return v.upper()
        return v.upper()

    zub_num: int = Field(..., example='80')
    vsheet: int = Field(..., example='200')
    hcountitem: int = Field(..., example='4')
    vcountitem: int = Field(..., example='5')
    hgap: condecimal(max_digits=10, decimal_places=4) = Field(..., example='3.3567')
    vgap: condecimal(max_digits=10, decimal_places=4) = Field(..., example='3.456')
    cf2: str = Field(None, example='ex_cut.cf2')
    mfg: str = Field(None, example='ex_cut.mfg')
    pict: str = Field(None, example='ex_cut.png')
    descript: str = Field(None, example='описание к штампу')


class DieCutGetListSchema(DieCutSchema):
    version_uuid: UUID = None
    created_on: datetime = None
    updated_on: datetime = None


class DieCutGetSinglSchema(DieCutSchema):
    version_uuid: UUID = None
    created_on: datetime = None
    updated_on: datetime = None


class DieCutCreateSchema(BaseModel):
    cut_name: str = Field(..., example='Ex_cut')
    zub_num: int = Field(..., example='80')
    vsheet: int = Field(..., example='200')
    hcountitem: int = Field(..., example='4')
    vcountitem: int = Field(..., example='5')
    hgap: condecimal(max_digits=10, decimal_places=4) = Field(..., example='3.3567')
    vgap: condecimal(max_digits=10, decimal_places=4) = Field(..., example='3.456')
    cf2: str = Field(None, example='ex_cut.cf2')
    mfg: str = Field(None, example='ex_cut.mfg')
    pict: str = Field(None, example='ex_cut.png')
    descript: str = Field(None, example='описание к штампу')


class Color(BaseModel):
    color_fullname: str

    class Config:
        orm_mode = True


class DesignPart(BaseModel):
    name: str
    descript: str
    colors: Optional[List[Color]]

    class Config:
        orm_mode = True


class Design(BaseModel):
    design_id: int
    design_num: str = Field(..., example='A001')
    parts: Optional[List[DesignPart]]

    class Config:
        orm_mode = True


class Customer(BaseModel):
    name: str
    descript: str

    class Config:
        orm_mode = True


class CustomerListSchema(Customer):
    id: int

    class Config:
        orm_mode = True


class RowFrame(BaseModel):
    descript: str
    design_url: str
    row_number: int
    design_angle_rotate: int

    class Config:
        orm_mode = True


class FrameDigitalJob(BaseModel):
    frame_num: int
    descript: str
    rows: Optional[List[RowFrame]] = None

    class Config:
        orm_mode = True


class DigitalJobPrint(BaseModel):
    digitaljob_num: str
    descript: str
    bleed: str
    razmeshenie: str
    color_print: str
    customer_id: int
    diecut_cut_name: str

    frames: Optional[List[FrameDigitalJob]] = None

    class Config:
        orm_mode = True


class DigitalJobTable(BaseModel):
    digitaljob_num: str = Field(example='05 1001')
    descript: str = Field(example='описание')
    customer: Optional[Customer] = Field(description='Заказчик')

    # diecut_cut_name: str

    # frames: Optional[List[FrameDigitalJob]] = None

    class Config:
        orm_mode = True
