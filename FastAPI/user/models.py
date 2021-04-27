from datetime import *

from sqlalchemy import Column, String, Integer, Text, DateTime, Float, DECIMAL, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship, backref

from core.db import Base


class Role(Base):
    # parent
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    # Relationships
    users_role = relationship('User', back_populates='role_user')  # parent


class User(Base):
    # children
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow())
    updated_on = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    # Нужен для security!
    is_active = Column(Boolean, default=True)
    description = Column(Text, nullable=True)
    # Relationships
    role_id = Column(Integer, ForeignKey('roles.id'), default=1)
    role_user = relationship('Role', back_populates='users_role', lazy='joined')

