import pyautogui
from time import sleep

pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False


class MouseControls:
    type = "pyautogui"

    @staticmethod
    def move(args):
        x, y = args
        pyautogui.moveTo(x, y)

    @staticmethod
    def move_click(args, wait=0):
        x, y = args
        pyautogui.moveTo(x, y)
        pyautogui.click()
        sleep(wait)

    @staticmethod
    def move_relative(rel_x, rel_y):
        pyautogui.moveRel(rel_x, rel_y)

    @staticmethod
    def click(wait=0):
        pyautogui.leftClick()
        sleep(wait)

    @staticmethod
    def get_position():
        point = pyautogui.position()
        return point.x, point.y

    @staticmethod
    def tab(number):
        sleep(2)
        for _ in range(number):
            pyautogui.press('tab')
            sleep(1)

    @staticmethod
    def enter():
        pyautogui.press("enter")
