import uuid
from datetime import *

from sqlalchemy import Column, String, Integer, Text, DateTime, Float, DECIMAL, ForeignKey, Boolean, Table, \
    create_engine

from sqlalchemy.orm import relationship, backref

from core.db import Base


class Zub(Base):
    __tablename__ = 'zubs'
    zub_num = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=False)
    '''номер зуба'''
    hprint = Column(DECIMAL(10, 4), unique=True, nullable=False)
    '''длина печати'''
    hpolimer = Column(DECIMAL(10, 4), unique=True, nullable=False)
    '''длина полимера 1,14'''
    hpolimer_17 = Column(DECIMAL(10, 4), unique=True, nullable=False)
    '''длина полимера 1,17'''
    diecuts = relationship('DieCut', backref=backref('zub'))
    '''номера штампов'''
    version_uuid = Column(String(32), default=lambda version: uuid.uuid4().hex,
                          onupdate=lambda version: uuid.uuid4().hex)
    '''столбец версии записи'''
    created_on = Column(DateTime(), default=datetime.utcnow())
    updated_on = Column(DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        super(Zub, self).__init__(*args, **kwargs)
        self.created_on = datetime.utcnow()
        self.version_uuid = lambda version: uuid.uuid4().hex

    __mapper_args__ = {
        'version_id_col': version_uuid,
        'version_id_generator': lambda version: uuid.uuid4().hex
    }


class DieCut(Base):
    __tablename__ = 'diecuts'
    cut_name = Column(String(60), primary_key=True, nullable=False)
    '''имя штампа'''
    zub_num = Column(Integer, ForeignKey('zubs.zub_num'), nullable=False)
    '''номер зуба'''
    vsheet = Column(Integer, nullable=False)
    '''ширина штампа'''
    hcountitem = Column(Integer, nullable=False)
    '''к-во этикеток по длине(направлению печати)'''
    vcountitem = Column(Integer, nullable=False)
    '''к-во этикеток поперёк печати'''
    hgap = Column(DECIMAL(10, 4), nullable=False)
    '''отступ между этикетками по длине(направлению печати)'''
    vgap = Column(DECIMAL(10, 4), nullable=False)
    '''отступ между этикетками поперёк печати'''
    cf2 = Column(String(255), nullable=True)
    mfg = Column(String(255), nullable=True)
    pict = Column(String(255), nullable=True)
    descript = Column(Text, nullable=True)
    version_uuid = Column(String(32), onupdate=lambda version: uuid.uuid4().hex)
    '''столбец версии записи'''
    created_on = Column(DateTime(), default=datetime.utcnow())
    updated_on = Column(DateTime(), onupdate=datetime.utcnow())

    digital_jobs_print = relationship('DigitalJobPrint', backref=backref('diecut'), lazy='joined')

    def __init__(self, *args, **kwargs):
        super(DieCut, self).__init__(*args, **kwargs)
        # self.created_on = self.created_on = datetime.utcnow()
        # self.version_uuid = lambda version: uuid.uuid4().hex
        self.upper_cut_name()

    def upper_cut_name(self):
        if self.cut_name:
            self.cut_name = self.cut_name.upper()

    __mapper_args__ = {
        'version_id_col': version_uuid,
        'version_id_generator': lambda version: uuid.uuid4().hex
    }


colors_to_parts_table = Table(
    'colors_to_parts_table',
    Base.metadata,
    Column('part_id', Integer(), ForeignKey('parts.part_id'), primary_key=True),
    Column('color_id', Integer(), ForeignKey('colors.color_id'), primary_key=True)
)


# # # # # # # Дизайны
class Color(Base):
    __tablename__ = 'colors'
    color_id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    color_fullname = Column(String(36), nullable=False, unique=True)
    parts = relationship('Part', secondary='colors_to_parts_table', back_populates='colors', lazy='joined')


class Part(Base):
    __tablename__ = 'parts'
    part_id = Column(Integer(), primary_key=True, unique=True)
    name = Column(String(45), nullable=False)
    descript = Column(Text)
    design_id = Column(Integer(), ForeignKey('designs.design_id'))
    colors = relationship('Color', secondary='colors_to_parts_table', back_populates='parts', lazy='joined')


class Design(Base):
    __tablename__ = 'designs'
    design_id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    design_num = Column(String(8), nullable=False, unique=True)
    parts = relationship('Part', backref='parts', lazy='joined')


# # # # # # # #


# # # # # # # Спуск на штамп для цифры
class RowFrame(Base):
    __tablename__ = 'rows_frame'
    row_id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    row_number = Column(Integer(), nullable=False)
    descript = Column(Text)
    frame_id = Column(Integer, ForeignKey('frames.frame_id', ondelete='CASCADE'), nullable=False)
    design_angle_rotate = Column(Integer(), default=0, nullable=False)
    design_url = Column(String(), nullable=False)


# Одна или много строк пренадлежит конкретному фрейму

class Frame(Base):
    __tablename__ = 'frames'
    frame_id = Column(Integer(), primary_key=True, unique=True)
    frame_num = Column(Integer(), nullable=False)
    descript = Column(Text)

    digitaljob_id = Column(Integer, ForeignKey('digital_jobs_print.digitaljob_id', ondelete='CASCADE'), nullable=False)
    rows = relationship('RowFrame',
                        backref=backref('rows', cascade="all,delete"),
                        lazy='joined',
                        single_parent=True,
                        )


# Один или много фреймов пренадлежит конкретному заказу

class DigitalJobPrint(Base):
    """
        descript : `str`
            Описание задания.        
        digitaljob_num : `str`
            номер задания.
        bleed : `str` 
            блид. По умолчанию 1,5. Число через запятую. 
        color_print : `str`
            Цветность печати. по умолчанию `CMYK`.  
        razmeshenie : `str`
            размещение этикеток: h - по строкам. v - по столбцам   
        diecut_cut_name : `str`
            номер штампа
        customer_id : `int`
            заказчик
    """
    __tablename__ = 'digital_jobs_print'
    digitaljob_id = Column(Integer(), primary_key=True, unique=True, autoincrement=True, nullable=False)
    digitaljob_num = Column(String(10), nullable=False, unique=True)
    descript = Column(Text)
    bleed = Column(String(3), default='1,5')
    razmeshenie = Column(String(1), default='h')  # размещение этикеток: h - по строкам. v - по столбцам
    color_print = Column(String(5), default='CMYK')  #

    diecut_cut_name = Column(String(60),
                             ForeignKey('diecuts.cut_name'),
                             nullable=False,
                             )
    frames = relationship('Frame',
                          backref=backref('frames', cascade="all,delete"),
                          lazy='joined',
                          single_parent=True,
                          )
    # Заказчик O2M (у одного заказчика, может быть много заказов)
    customer_id = Column(Integer,
                         ForeignKey('customers.id'))


# # # # # # # #


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(), nullable=False, unique=True)
    descript = Column(Text)

    digitaljobs = relationship('DigitalJobPrint',
                               backref='customer'
                               )
