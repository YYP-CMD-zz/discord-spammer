import pyautogui
import time
import webbrowser


message = input("message content: (leave blank if u want to use ur clipboard)")
repeats = int(input('How many Messages:'))
delay = int(input('how much delay:'))


isLoaded = input("load discord then press enter")

print("five seconds until spam")

time.sleep(5)

for i in range (0,repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

    time.sleep(delay/1000)