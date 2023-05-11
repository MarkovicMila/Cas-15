import pyautogui as pg

print(pg.position())
print(pg.size())
print(pg.onScreen(1080,520))
pg.PAUSE=2.5
pg.FAILSAFE=True