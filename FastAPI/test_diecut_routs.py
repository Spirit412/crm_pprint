from fastapi.testclient import TestClient
from main import app
import sys
from loguru import logger
fmt = "<green>{time}</green> - {name} - {level} - {message}"

logger.add(sys.stderr, format=fmt, filter="my_module", level="INFO", backtrace=True,
           diagnose=True, colorize=True)
# logger.level("CUSTOM", no=45, color="<red>", icon="🚨")

client = TestClient(app)

cut = {
    "cut_name": "cut_pytest",
    "zub_num": 89,
    "vsheet": 155,
    "hcountitem": 3,
    "vcountitem": 1,
    "hgap": "4.1900",
    "vgap": "0.0000",
    "cf2": "файл cf2",
    "mfg": "файл MFG",
    "pict": "файл картинки",
    "descript": "тест"
}
plus_version_url_api = '/api/v1'

def test_get_cut():
    logger.info('eggs info')
    logger.warning('eggs warning')
    logger.error('eggs error')
    logger.critical('eggs critical')

    response = client.get(f"{plus_version_url_api}/diecuts/{cut['cut_name']}")
    # LOGGER.info(f'Ответ сервера: {response}')

    data = response.json()
    logger.info(f'Получаем данные по штампу из БД в формате json: {data}')

    if response.status_code == 200 and data['cut_name'] == cut['cut_name'].upper():
        # """Штам есть. Удаляем"""
        delete(cut['cut_name'].upper())
        create(cut)
        update(cut)
        delete(cut['cut_name'].upper())
    else:
        # """Штампа нет. Создаём"""
        create(cut)
        update(cut)
        delete(cut['cut_name'].upper())


def delete(id):
    logger.info(f"Штам {id}. Удаляем")
    # assert response.status_code == 200
    response = client.delete(f"{plus_version_url_api}/diecuts/{id}")
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


