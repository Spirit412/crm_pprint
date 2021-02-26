import uuid
from datetime import *

from sqlalchemy import Column, String, Integer, Text, DateTime, Float, DECIMAL, ForeignKey, Boolean, Table
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

    def __init__(self, *args, **kwargs):
        super(DieCut, self).__init__(*args, **kwargs)
        self.created_on = self.created_on = datetime.utcnow()
        self.upper_cut_name()
        self.version_uuid = lambda version: uuid.uuid4().hex

    def upper_cut_name(self):
        if self.cut_name:
            self.cut_name = self.cut_name.upper()

    __mapper_args__ = {
        'version_id_col': version_uuid,
        'version_id_generator': lambda version: uuid.uuid4().hex
    }
