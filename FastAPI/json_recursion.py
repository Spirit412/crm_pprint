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
            "descript": "описание фрейма 1",
            "rows": [
                {
                    "descript": "описание 1 строки, фрейм #1",
                    "design_url": "\\\\TS\\Obmen\\190001__ED.pdf",
                    "row_number": 1,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 2 строки, фрейм #1",
                    "design_url": "\\\\TS\\Obmen\\190001__ED.pdf",
                    "row_number": 2,
                    "design_angle_rotate": 0
                }
            ]
        },
        {
            "frame_num": 2,
            "descript": "описание фрейма 2",
            "rows": [
                {
                    "descript": "описание 1 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200001__ED.pdf",
                    "row_number": 1,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 2 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200002__ED.pdf",
                    "row_number": 2,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 3 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200003__ED.pdf",
                    "row_number": 3,
                    "design_angle_rotate": 0
                },
                {
                    "descript": "описание 4 строки, фрейм #2",
                    "design_url": "\\\\TS\\Obmen\\200004__ED.pdf",
                    "row_number": 4,
                    "design_angle_rotate": 0
                }
            ]
        }
    ]
}

for frame in data['frames']:
    rows = []
    frames = []
    
    for row in frame['rows']:
        frames.append(frame)
        rows.append(row)
    # del frame['rows']
    print(rows, '\n')
    print('ФРЕЙМ:', frames, '\n')
        # rows.append(row)
    # for row in rows:
    #     print(row, '\n')
    # for frame in frames:
    #     del frame['rows']
    #     print('ФРЕЙМ:', frame, '\n')

        # print(frames)

# row_frame1 = [
#     models.RowFrame(row_number=1, descript='описание 1 строки 1 фр', design_url='\\\\TS\\Obmen\\190001__ED.pdf',
#                     design_angle_rotate=0),
#     models.RowFrame(row_number=2, descript='описание 2 строки 1 фр', design_url='\\\\TS\\Obmen\\190001__ED.pdf',
#                     design_angle_rotate=0)]
# row_frame2 = [
#     models.RowFrame(row_number=1, descript='описание 1 строки 2 фр', design_url='\\\\TS\\Obmen\\200002__ED.pdf',
#                     design_angle_rotate=0),
#     models.RowFrame(row_number=2, descript='описание 2 строки 2 фр', design_url='\\\\TS\\Obmen\\200002__ED.pdf',
#                     design_angle_rotate=0)]
# frames_job = [models.Frame(frame_num=1, descript='описание фрейма1', rows=[*row_frame1]),
#               models.Frame(frame_num=2, descript='описание фрейма2', rows=[*row_frame2])]
# digitaljob = models.DigitalJobPrint(digitaljob_num='05 0001', descript='описание', bleed='1.5', razmeshenie='h',
#                                     color_print='cmyk', diecut_cut_name='A224', customer_id=8, frames=[*frames_job]
#                                     )
# db.add(digitaljob)
# db.commit()
