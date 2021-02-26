import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_url_db():
    if sys.platform.startswith('linux'):
        URL = "postgresql://postgres:postgres@10.5.0.5:5432/fastapi"
        # для доступа к БД из контейнера IPAddress
    else:
        URL = "postgresql://postgres:postgres@localhost:6532/fastapi"
        # для доступа к БД из вне
    return URL


SQLALCHEMY_DATABASE_URL = get_url_db()

engine = create_engine(get_url_db())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
