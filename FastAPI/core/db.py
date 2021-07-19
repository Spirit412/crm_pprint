import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging

logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
# logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)
# logging.getLogger("sqlalchemy.pool").setLevel(logging.INFO)
#logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


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
#echo = True,  # выводить запросы в консоль 
# echo_pool='debug'

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
Base = declarative_base()
