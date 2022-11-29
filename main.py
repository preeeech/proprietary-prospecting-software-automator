import pyautogui
import time



scrollbar = (908,235)

tagposition = (1730,737)

listposition = (457,54)

refreshposition = (11,155)

scrollbarincrement = scrollbar[1]
time.sleep(5)


while True:
    buttonlocation = pyautogui.locateOnScreen("white_box.png")

    if buttonlocation is not None:
        buttonx, buttony = pyautogui.center(buttonlocation)
        pyautogui.doubleClick(buttonx, buttony)
        time.sleep(3)
        pyautogui.click(*tagposition)
        time.sleep(3)
        pyautogui.click(*listposition)
        time.sleep(3)
        pyautogui.click(*refreshposition)
        scrollbarincrement = scrollbar[1]

    scrollbarincrement += 70
    pyautogui.moveTo(scrollbar[0], scrollbarincrement)
    pyautogui.dragTo(scrollbar[0], scrollbarincrement + 65, button="left")

    if scrollbarincrement >= 1000:
        pyautogui.click(*refreshposition)
        scrollbarincrement = scrollbar[1]
