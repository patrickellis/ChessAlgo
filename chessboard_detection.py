import numpy as np
import cv2
import pyautogui
import PIL.ImageShow as im
import mss

from PIL import Image

def find_chessboard():
    screenshot_shape = np.array(pyautogui.screenshot()).shape
    sct = mss.mss()
    monitor = {'top': 173, 'left': 3907, 'width': 800, 'height': 800}
    img = sct.grab(monitor)
    img_frombytes = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
    im.show(img_frombytes)


find_chessboard()
