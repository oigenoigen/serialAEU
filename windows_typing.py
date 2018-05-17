import win32api
import win32con
import time
print("FuckinggitIcannotgethowtoworkhere")
args = "34546546.345.345"
for i in args:
    if i==".":
        key=190#i hate fucking windows
    else:
        key=ord(i)
    win32api.keybd_event(key, 0, 0, 0)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
