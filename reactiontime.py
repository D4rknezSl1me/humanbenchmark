import pyautogui as pag
import time

green = (75, 219, 106)

while True:
    x, y = pag.position()
    px = pag.pixel(x, y)
    if(px==green):
        pag.click()
