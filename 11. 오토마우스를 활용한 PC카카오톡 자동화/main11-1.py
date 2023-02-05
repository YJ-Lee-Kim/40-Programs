import pyautogui

picPosition = pyautogui.locateOnScreen(r"11. 오토마우스를 활용한 PC카카오톡 자동화\카카오톡_내사진1.png")
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r"11. 오토마우스를 활용한 PC카카오톡 자동화\카카오톡_내사진2.png")
    print(picPosition)
    
if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r"11. 오토마우스를 활용한 PC카카오톡 자동화\카카오톡_내사진3.png")
    print(picPosition)