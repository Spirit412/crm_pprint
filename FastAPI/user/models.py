from datetime import *

from sqlalchemy import Column, String, Integer, Text, DateTime, Float, DECIMAL, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship, backref

from core.db import Base

class Role(Base):
    # parent
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(String(255))
    user = relationship('User', backref=backref('roles'))  # parent


class User(Base):
    # children
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    name = Column(String(100), unique=True)
    password = Column(String(255))
    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    # Нужен для security!
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    # Для получения доступа к связанным объектам
    # roles = relationship('Role', secondary=roles_users, backref=backref('users', lazy='dynamic'))
    role_id = Column(Integer, ForeignKey('roles.id'))  # children
    role = relationship('Role', back_populates="role")
