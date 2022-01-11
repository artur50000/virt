import pyautogui
import pywinauto
from pywinauto.application import Application
import keyboard
from datetime import datetime
from activity import find_image,click_near_image
import os
from PIL import Image
import time

start = datetime.now()

image_dict = {}


folder = "D:/rpa/"
'''
for file in os.listdir(folder):
    
    if file.endswith(".png") or file.endswith("PNG"):
        image_dict[file[:-4]] = Image.open(f"{folder}{file}")
        

'''
image_dict = {file[:-4]:Image.open(f"{folder}{file}")
              for file in os.listdir(folder)
              if file.endswith(".png")
              or file.endswith("PNG")}


#print(image_dict)

app = Application(backend="uia").start('C:\TCML\TOTALCMD64.EXE')

but1 = find_image(image_dict['conf'], 0.6)


pyautogui.click(but1)
#print(but1)

but2 = find_image(image_dict['panel'], 0.6)
pyautogui.click(but2)

pos = click_near_image(image_dict['filezn1'], 0.9, 60, 0)
pyautogui.click(pos)
#print(but3)
#print(pos)

keyboard.write("ssdfds")

end = datetime.now()

fin = end - start
print(fin)