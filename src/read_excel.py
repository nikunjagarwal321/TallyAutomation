import datetime
import xlrd
from sale_detail import SaleDetail


def open_sheet(location):
    workbook = xlrd.open_workbook(location) 
    sheet = workbook.sheet_by_index(0) 
    return workbook, sheet

def get_readable_date(date_float, workbook):
    year, month, day, hour, min, sec = xlrd.xldate_as_tuple(date_float, workbook.datemode)
    date = str(day) + '-' + str(month) + '-' + str(year)

def get_sales_data(location):
    workbook, sheet = open_sheet(location)
    sales_data_list = {}
    print(sheet.nrows)
    for i in range(6,sheet.nrows):
        date_float = sheet.cell_value(i,0)
        date = get_readable_date(date_float, workbook)
        party_name = sheet.cell_value(i,1)
        voucher_no = sheet.cell_value(i,3)
        amount = sheet.cell_value(i,4)
        sale_detail = SaleDetail(party_name, amount, voucher_no)
        sales_data_list[date] = []
        sales_data_list[date].append(sale_detail)
    return sales_data_list
