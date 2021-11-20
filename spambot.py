import  pyautogui
import webbrowser as web
from time import sleep

web.open("https://web.whatsapp.com/send?phone=+523311325689")
sleep(10)

#with open("Holi.txt", "r") as file:
#    for line in file:
#        pyautogui.typewrite(line)
#        pyautogui.press("enter")

for i in range(10):
    pyautogui.typewrite("Hola Bro!\nVamos por los tacos")
    pyautogui.press("enter")