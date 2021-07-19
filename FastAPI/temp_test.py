import json

json_db = {
    "diecut_cut_name": "A1001",
    "bleed": "1.5",
    "razmeshenie": "h",
    "digitaljob_num": "05 2003",
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
                    "design_url": "\\\\TS\\Obmen\\190002__ED.pdf",
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
                },
                {
                    "descript": "описание 3 строки 2 фр",
                    "design_url": "\\\\TS\\Obmen\\200003__ED.pdf",
                    "row_number": 3,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 4 строки 2 фр",
                    "design_url": "\\\\TS\\Obmen\\200004__ED.pdf",
                    "row_number": 4,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 5 строки 2 фр",
                    "design_url": "\\\\TS\\Obmen\\200005__ED.pdf",
                    "row_number": 5,
                    "design_angle_rotate": 0
                }
            ]
        }
    ]
}


def gel_key_is_list(json: object) -> list:
    list_key_is_list = []
    for key in json.keys():
        if isinstance(json[key], (list, dict)):
            list_key_is_list.append(key)

    return list_key_is_list


test_data = json_db.copy()
print('///////  ', gel_key_is_list(test_data), end='\n')

for item in gel_key_is_list(test_data):
    # print('--' * 5, '|', test_data[item], end='\n')
    for jframe in range(len(test_data[item])):
        print('--' * 5, '|', jframe, end='\n')
        print(test_data[item][jframe])
        # for kitem in range(len(gel_key_is_list(test_data[item][jframe]))):
        #     print('  ' * 5, '|', '--' * 5, len(gel_key_is_list(jframe)), end='\n')
