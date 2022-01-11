import pyautogui
import sys
import time
import cv2
from settings import folder
from PIL import Image


def find_image(image, conf):
    """
    function that returns image position to click
    arguments:
    image - image file
    conf - opencv sensibility
    """
    try:
        #path = Image.open(f"{folder}{image}")
        image_to_find = pyautogui.locateOnScreen(image, confidence=conf)
        i = 0

        while not image_to_find:
            i += 1
            time.sleep(1)
            print(f"{i} attempt {image}")
            image_to_find = pyautogui.locateOnScreen(image, confidence=conf)
            if i > 3:
                sys.exit(f"image {image} not found!")
        
        return image_to_find
    except IOError as e:
        sys.exit(e)


def click_near_image(image, conf, shift_x, shift_y):
    """
    function that returns position to click
    near defined image
    arguments:
    image - image file
    conf - opencv sensibility
    shift_x - shift from image x coordinate
    shift_y - shift from image y coordinate
    """

    but3 = find_image(image, conf)
    buttonpoint = pyautogui.center(but3)
    pyautogui.moveTo(buttonpoint.x + shift_x, buttonpoint.y + shift_y) 
    pos = pyautogui.position()
    return pos