import pyscreeze
import PIL
__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION
import pyautogui
import cv2
import numpy as np



Factor = 2
while True:
    cv2.waitKey(3000)
    try:
        location = pyautogui.locateCenterOnScreen('Accept.png', confidence = 0.7)
    except pyautogui.ImageNotFoundException:
        continue
    if location is None:
        continue
    x = location.x//Factor
    y = location.y//Factor
    pyautogui.moveTo(x, y)
    pyautogui.click()
