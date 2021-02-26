Миграции
`alembic revision --autogenerate -m "version 14"`
`alembic upgrade head`


PYTEST
Использую команзу 
`python -m pytest`
Тогда импортируются модули

Узнать IP подключения к БД
`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_cont`