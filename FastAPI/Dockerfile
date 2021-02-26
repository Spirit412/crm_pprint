FROM python:3.8

ARG APP_DIR=app_fastapi
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /${APP_DIR}
COPY . /${APP_DIR}

# ENV FASTAPI_ENV = "app_fastapi"
# install dependencies

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt
RUN pip install -r /${APP_DIR}/req.txt

# VOLUME .:/app_fastapi

CMD python main.py

EXPOSE 8000
