import time
import win32api, win32gui, win32con
import Constant


def mouse_move(x, y, speed = 0):
    if speed is 0:
        #win32api.SetCursorPos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    else:
        (actualX, actualY) = mouse_position()
        aimX = x
        aimY = y

        while True:
            if actualX > aimX:
                actualX -= speed
            elif actualX < aimX:
                actualX += speed

            if actualY > aimY:
                actualY -= speed
            elif actualY < aimY:
                actualY += speed

            mouse_move(actualX, actualY)

            if actualX > (aimX - speed) and actualX < (aimX + speed):
                if actualY > (aimY - speed) and actualY < (aimY + speed):
                    break

            #if (x, y) is not mouse_position():
                #mouse_move(x, y)


def mouse_click(button = Constant.LEFT_MOUSE_BUTTON, repeat = 1, delay = 0.012):
    button = translate_to_win32(button)
    if repeat > 1:
        while repeat > 0:
            mouse_click(button)
            time.sleep(delay)
            repeat -= 1
    else:
        win32api.mouse_event(button, 0, 0, 0, 0)
        win32api.mouse_event(button*2, 0, 0, 0, 0)


def mouse_down(button = Constant.LEFT_MOUSE_BUTTON):
    button = translate_to_win32(button)
    win32api.mouse_event(button, 0, 0, 0, 0)


def mouse_up(button = win32con.MOUSEEVENTF_LEFTDOWN):
    button = translate_to_win32(button)
    win32api.mouse_event(button*2, 0, 0, 0, 0)


def mouse_wheel(amount):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, amount, 0)


def mouse_position():
    return win32gui.GetCursorPos()


def translate_to_win32(button):
    if (button == Constant.LEFT_MOUSE_BUTTON):
        return win32con.MOUSEEVENTF_LEFTDOWN
    elif (button == Constant.RIGHT_MOUSE_BUTTON):
        return win32con.MOUSEEVENTF_RIGHTDOWN
    elif (button == Constant.MIDDLE_MOUSE_BUTTON):
        return win32con.MOUSEEVENTF_MIDDLEDOWN