from fastapi.testclient import TestClient
from main import app
import sys
from loguru import logger

fmt = "<green>{time}</green> - {name} - {level} - {message}"

logger.add(sys.stderr, format=fmt, filter="my_module", level="INFO", backtrace=True,
           diagnose=True, colorize=True)
# logger.level("CUSTOM", no=45, color="<red>", icon="🚨")

client = TestClient(app)


item = {
    "descript": "описание выборжец",
    "name": "Выборжец",
}
plus_version_url_api = '/api/v1'


def test_get_costumer():
    logger.info('eggs info')
    logger.warning('eggs warning')
    logger.error('eggs error')
    logger.critical('eggs critical')

    response = client.get(f"{plus_version_url_api}/customer/{item['name']}")
    # LOGGER.info(f'Ответ сервера: {response}')

    data = response.json()
    logger.info(f'Получаем данные по штампу из БД в формате json: {data}')

    if response.status_code == 200 and data['name'] == item['name'].upper():
        # """Штам есть. Удаляем"""
        delete(item['name'].upper())
        create(item)
        update(item)
        delete(item['name'].upper())
    else:
        # """Штампа нет. Создаём"""
        create(item)
        update(item)
        delete(item['name'].upper())


def delete(id):
    logger.info(f"Штам {id}. Удаляем")
    # assert response.status_code == 200
    response = client.delete(f"{plus_version_url_api}/customer/diecuts/{id}")
    assert response.status_code == 200


def create(id: dict):
    logger.info(f"Создаём штамп \n {id['cut_name']}")
    response = client.post(f"{plus_version_url_api}/diecuts/",
                           json=id
                           )
    assert response.status_code == 201
    # Проверяем
    logger.info("Проверям созданный штамп")
    data = response.json()
    logger.info(f"Данные из БД созданного штампа \n {data}")
    assert 'zub_num' in data
    assert 'cut_name' in data

    assert data['cut_name'] == id['cut_name'].upper()
    assert data['zub_num'] == 89
    assert data['hgap'] == float("4.1900")


def update(id: dict):
    id['descript'] = 'test update'
    id['cf2'] = 'файл CF2 обновили'
    id['hgap'] = 9
    id['vgap'] = 9
    logger.info(f"данные на обновление: {id}")
    response = client.patch(f"{plus_version_url_api}/diecuts/{id['cut_name']}",
                            json=id
                            )
    # assert response.status_code == 200
    # Проверяем
    logger.info("Проверям обновлённый штамп")
    data = response.json()
    logger.info(f"Данные штампа после обновления \n {data}")
    assert data['descript'] == 'test update'
    assert data['cf2'] == 'файл CF2 обновили'
    assert data['hgap'] == 9
    assert data['vgap'] == 9
