import pyautogui as gui
import time

def goto_vouchers():
    gui.press('v')
    time.sleep(1)
    gui.press('F6')
    time.sleep(1)

def input_single_entry(sale_detail):
    gui.write(sale_detail.party_name)
    gui.press('enter')
    time.sleep(0.25)
    gui.write(sale_detail.amount)
    gui.press('enter')
    time.sleep(0.25)
    gui.write('agst ref')
    gui.press('enter')
    time.sleep(0.25)
    gui.write(sale_detail.voucher_no)
    gui.press('enter')
    time.sleep(0.25)
    gui.write(sale_detail.amount)
    gui.press('enter')
    time.sleep(0.25)
    gui.write('Cr')
    gui.press('enter')       
    time.sleep(0.25)

def update_day_receipt(date, sale_details):
    gui.press('f2')
    time.sleep(0.25)
    gui.write(date)
    gui.press('enter')
    time.sleep(0.25)
    gui.write('cash')
    gui.press('enter')
    time.sleep(0.25)
    for sale_detail in sale_details:
        # Enter Ledgers whose entry is not to be done
        if sale_detail.party_name not in []:    
            input_single_entry(sale_detail)
    gui.press('enter')
    gui.press('enter')
    gui.press('y')
    time.sleep(3)


def close_tally():
    for _ in range(2):
        gui.press('esc',interval=0.25)
    gui.press('y')

def update_all_receipt(data_dict):
    goto_vouchers()
    for key, value in data_dict:
        update_day_receipt(key, value)
    close_tally()
