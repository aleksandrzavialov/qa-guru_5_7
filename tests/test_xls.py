import os
import xlrd
from conftest import PROJECT_RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_xls_processing():
    xls_file = os.path.join(PROJECT_RESOURCE_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file)
    print(f'Количество листов {book.nsheets}')
    assert book.nsheets == 1
    print(f'Имена листов {book.sheet_names()}')
    assert book.sheet_names().__getitem__(0) == 'Sheet1'
    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    assert sheet.ncols == 8
    print(f'Количество строк {sheet.nrows}')
    assert sheet.nrows == 10
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=8, colx=1)}')
    assert sheet.cell_value(rowx=8, colx=1) == 'Earlean'
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))
