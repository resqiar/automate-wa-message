import pywhatkit
import pyautogui
import time

phone = '+6281288381102'
msg = """


(This message is sent automatically with ❤️ by *Rescue*)
"""
hour = 19
minute = 5
waitFor = 30 # in seconds

# sent message to 
pywhatkit.sendwhatmsg(phone, msg, hour, minute, waitFor)

time.sleep(5)

# CLOSE THE TAB
pyautogui.hotkey('ctrl', 'f4')