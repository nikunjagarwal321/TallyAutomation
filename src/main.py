import pyautogui as gui
import time
from TallyProject import export_excel  
from TallyProject import read_excel
from TallyProject import update_receipt


def open_tally(x1, y1):
    gui.click(clicks=2, x=x1, y=y1)
    time.sleep(10)

def main():
    location = ("C:\Program Files\Tally\Tally.ERP9\DayBook.xlsx")
    icon_x = 167
    icon_y = 539  
    no_of_past_months = 0
    # Export sales details
    open_tally(icon_x, icon_y)
    export_excel.export_sales(no_of_past_months)
    export_excel.close_tally()
    time.sleep(10)
    # Read sales data
    sales_data_list = read_excel.get_sales_data(location)
    # Update receipt
    open_tally()
    update_receipt.update_all_receipt(sales_data_list)
    update_receipt.close_tally()

if __name__=='__main__':
    main()

    
