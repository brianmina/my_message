import pyautogui
from shift_tab import shift_tab

print(pyautogui.position()) # in a screen of 1920x1080 resolution 
pyautogui.PAUSE = 1
pyautogui.click(x=24,y=1060)

pyautogui.PAUSE = 1
pyautogui.press("tab", presses=8)

pyautogui.PAUSE = 1
pyautogui.write("google chrome")

pyautogui.PAUSE = 1
pyautogui.press("enter")

pyautogui.PAUSE = 1
pyautogui.write("https://web.whatsapp.com/")

pyautogui.PAUSE = 6
pyautogui.press("enter")

pyautogui.PAUSE = 0.005
shift_tab(7)


pyautogui.write("Prada")
pyautogui.press("enter")
pyautogui.write("**Testing program...*")
pyautogui.press("enter")





    