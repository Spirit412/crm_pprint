Миграции
`alembic revision --autogenerate -m "version 14"`
`alembic upgrade head`


PYTEST
Использую команзу
`python -m pytest`
Тогда импортируются модули

Узнать IP подключения к БД
`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_cont`

Docker-compose 
~~запуск
 `docker-compose up --build`
 ~~остановка
 `docker-compose down`
 
 логи контейнера
``` docker logs container --tail 30 --follow ```