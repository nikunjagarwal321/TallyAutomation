import pyautogui as gui
import time

def goto_sales_register():
    gui.write('das', interval=0.5)
    time.sleep(2)

def export_sales(no_of_past_months):
    goto_sales_register()
    for _ in range(no_of_past_months):
        gui.press('up')
    gui.press('enter')
    time.sleep(2)
    gui.hotkey('alt','e')
    time.sleep(2)
    gui.press('enter')
    time.sleep(10)

def close_tally():
    for _ in range(5):
        gui.press('esc',interval=0.25)
    gui.press('y')
