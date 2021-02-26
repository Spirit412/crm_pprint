import pytest
from httpx import AsyncClient

from .main import app

BASE_URL_DIECUTS = "http://127.0.0.1:8000/diecuts"
payload = {}
headers = {}

cut = {
    "cut_name": "cut_pytest",
    "zub_num": 89,
    "vsheet": 155,
    "hcountitem": 3,
    "vcountitem": 1,
    "hgap": "4.1900",
    "vgap": "0.0000",
    "cf2": "",
    "mfg": "",
    "pict": "",
    "descript": ""
}


# Чтение из БД

@pytest.mark.asyncio
async def test_get_cut():
    async with AsyncClient(app=app, base_url=BASE_URL_DIECUTS) as ac:
        response = await ac.get(f"/{cut['cut_name']}")
        if response.status_code == 200:
            assert response.status_code == 200
            await test_delete_cut()
            print('уже есть')
        # assert response.status_code is not 200
        else:
            assert response.status_code == 404
            await test_create_cut()
            print('нет')


@pytest.mark.asyncio
async def test_delete_cut():
    async with AsyncClient(app=app, base_url=BASE_URL_DIECUTS) as ac:
        response = await ac.delete(f"/{cut['cut_name']}")
        assert response.status_code == 200
        print('DELETE')


@pytest.mark.asyncio
async def test_create_cut():
    async with AsyncClient(app=app, base_url=BASE_URL_DIECUTS) as ac:
        response = await ac.post("/", json=cut)
        assert response.status_code == 201
        data = response.json()
        print('CREATE')
        print(data)


@pytest.mark.asyncio
async def test_delete_cut():
    async with AsyncClient(app=app, base_url=BASE_URL_DIECUTS) as ac:
        response = await ac.delete(f"/{cut['cut_name']}")
        assert response.status_code == 200
        print('DELETE')

