from fastapi.testclient import TestClient
from main import app
import sys
from loguru import logger
import time


fmt = "<green>{time}</green> - {name} - {level} - {message}"

logger.add(sys.stderr, format=fmt, filter="my_module", level="INFO", backtrace=True,
           diagnose=True, colorize=True)
# logger.level("CUSTOM", no=45, color="<red>", icon="🚨")

client = TestClient(app)


data_json_test = {
    "diecut_cut_name": "A224",
    "bleed": "1.5",
    "razmeshenie": "h",
    "digitaljob_num": "05 0000",
    "customer_id": 8,
    "color_print": "cmyk",
    "descript": "описание",
    "frames": [
        {
            "frame_num": 1,
            "descript": "описание фрейма1",
            "rows": [
                {
                    "descript": "описание 1 строки 1 фр",
                    "design_url": "\\\\TS\\Obmen\\190001__ED.pdf",
                    "row_number": 1,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 2 строки 1 фр",
                    "design_url": "\\\\TS\\Obmen\\190001__ED.pdf",
                    "row_number": 2,
                    "design_angle_rotate": 0
                }
            ]
        },
        {
            "frame_num": 2,
            "descript": "описание фрейма2",
            "rows": [
                {
                    "descript": "описание 1 строки 2 фр",
                    "design_url": "\\\\TS\\Obmen\\200002__ED.pdf",
                    "row_number": 1,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 2 строки 2 фр",
                    "design_url": "\\\\TS\\Obmen\\200002__ED.pdf",
                    "row_number": 2,
                    "design_angle_rotate": 0
                }
            ]
        }
    ]
}

plus_version_url_api = '/api/v1'


def create(data_input: dict) -> dict:
    logger.info(f"Создаём штамп \n {data_input['digitaljob_num']}")
    
    response = client.post(f"{plus_version_url_api}/djob/",
                           json=data_input
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


def test_digital_job():
    
    # logger.info('eggs info')
    # logger.warning('eggs warning')
    # logger.error('eggs error')
    # logger.critical('eggs critical')
    
    
    frames = data_json_test['frames']
    for frame in frames:
        print('\n', 'F R A M E >>>>>>>>>>> ', *frame, end='\n\n')
        rows_in_frame = frame['rows']
        for row in rows_in_frame:
            print('R O W >>>>>>>>>>> ', row, end='\n')




    # print('\n\n\n', 'Такой DJOB data_input:', data_input['digitaljob_num'])

    # data_model = models.DigitalJobPrint(**item.dict())
    # print(data_model)
    # 
    # def test_add_djob():
    #     row_frame1 = [
    #         models.RowFrame(row_number=1, descript='описание 1 строки 1 фр', design_url='\\\\TS\\Obmen\\100001__ED.pdf',
    #                         design_angle_rotate=0),
    #         models.RowFrame(row_number=2, descript='описание 2 строки 1 фр', design_url='\\\\TS\\Obmen\\100002__ED.pdf',
    #                         design_angle_rotate=0)]
    # 
    #     row_frame2 = [
    #         models.RowFrame(row_number=1, descript='описание 1 строки 2 фр', design_url='\\\\TS\\Obmen\\200001__ED.pdf',
    #                         design_angle_rotate=0),
    #         models.RowFrame(row_number=2, descript='описание 2 строки 2 фр', design_url='\\\\TS\\Obmen\\200002__ED.pdf',
    #                         design_angle_rotate=0)]

    #     frames_job = [models.Frame(frame_num=1, descript='описание фрейма1', rows=[*row_frame1]),
    #                   models.Frame(frame_num=2, descript='описание фрейма2', rows=[*row_frame2])]
    #     print(frames_job)
    #     digitaljob = models.DigitalJobPrint(digitaljob_num='05 0001', descript='описание', bleed='1.5', razmeshenie='h',
    #                                         color_print='cmyk', diecut_cut_name='A224', customer_id=8,
    #                                         frames=[*frames_job]
    #                                         )
    #     print(digitaljob)
    # 
    #     db.add(digitaljob)
    #     db.commit()