from CheckWord import CheckWord
from EventCloud import EventCloud
import xlrd

def main(pos):
    xls_data = xlrd.open_workbook('worktime.xlsx')
    data_list = []
    table = xls_data.sheets()[0]
    for i in range(table.nrows):
        data_list.append(table.cell(i, 4).value)
    data_list.remove('Event')
    data = " ".join(data_list)
    a = CheckWord(pos)
    b = EventCloud()
    b.to_png(a.check_pos(data))

if __name__ == '__main__':
    main("err")
