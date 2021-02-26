from fastapi.testclient import TestClient
from main import app
import logging

LOGGER = logging.getLogger(__name__)

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
    "mfg": "файл ЬАП",
    "pict": "файл картинки",
    "descript": "тест "
}
plus_version_url_api = '/api/v1'

def test_get_cut():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')

    response = client.get(f"{plus_version_url_api}/diecuts/{cut['cut_name']}")
    LOGGER.info(f'Ответ сервера: {response}')

    data = response.json()
    LOGGER.info(f'Ответ в формате json: {data}')

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
    LOGGER.info(f"Штам {id}. Удаляем")
    # assert response.status_code == 200
    response = client.delete(f"{plus_version_url_api}/diecuts/{id}")
    assert response.status_code == 200


def create(id: dict):
    LOGGER.info(f"Создаём штамп {id['cut_name']}")
    response = client.post(f"{plus_version_url_api}/diecuts/",
                           json=id
                           )
    assert response.status_code == 201
    # Проверяем
    LOGGER.info("Проверям созданный штамп")
    data = response.json()
    assert 'zub_num' in data
    assert 'cut_name' in data

    assert data['cut_name'] == id['cut_name'].upper()
    assert data['zub_num'] == 89
    assert data['hgap'] == float("4.1900")


def update(id: dict):
    LOGGER.info(f"Обновляем штамп {id['cut_name']}")
    id['descript'] = 'test update'
    response = client.patch(f"{plus_version_url_api}/diecuts/{id['cut_name']}",
                           json=id
                           )
    assert response.status_code == 200
    # Проверяем
    LOGGER.info("Проверям обновлённый штамп")
    data = response.json()
    LOGGER.info(f"проверка описания {data}")
    # assert data['descript'] == 'test update'


