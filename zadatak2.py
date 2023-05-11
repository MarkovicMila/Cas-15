import pyautogui as pg
from time import sleep

# screenshot
# pg.hotkey('win','shift','s')
# sleep(2)
# pg.mouseDown(x=100,y=100,button='left')
# pg.mouseUp(x=200,y=200,button='left')

# word
pg.hotkey('win')
sleep(1)
pg.typewrite('word')
pg.hotkey('enter')
sleep(1)
pg.hotkey('F12')
