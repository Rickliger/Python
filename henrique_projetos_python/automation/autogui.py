import pyautogui

screenWidht, screenHeigth = pyautogui.size()

print(screenWidht, screenHeigth)

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)

#pyautogui.moveTo(100, 150)
#pyautogui.click(100, 150)
