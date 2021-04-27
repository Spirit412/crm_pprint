import json
data = {
    "diecut_cut_name": "A224",
    "bleed": "1.5",
    "razmeshenie": "h",
    "digitaljob_num": "05 0001",
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
frames = data['frames']
for frame in frames:
    print('\n', 'F R A M E >>>>>>>>>>> ', *frame, end='\n\n')
    rows_in_frame = frame['rows']
    for row in rows_in_frame:
        print('R O W >>>>>>>>>>> ', row, end='\n')
