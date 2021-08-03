import os
os.system("pip install tqdm")
import tqdm
import ctypes
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
import time

gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))

def move(y, x):
   value = x + (y << 16)
   ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))

def addstr(string):
   ctypes.windll.kernel32.WriteConsoleW(gHandle, c_wchar_p(string), c_ulong(len(string)), c_void_p(), None)

print("Loading SANDSEA ...")

print("Done!\n")

time.sleep(1)

move(0, 0)

for x in range(100):
    for x in range(10):
        print("                                                                                                     ")

move(0, 0)

print("\n |  SANDSEA Simulation Engine v." + str(open("E:/sandsea/SANDSEA-se-1/SANDSEA/currentVersion.ssd").read()).strip() + " Console    | ")
print(" | Command console open. If you need info on commands  | \n | and how to use them, you can check the HOWTO.md     |\n | file at the root!                                   |\n")

commandTypes = {
    "$": "3-space simulation modification command",
    "?": "query request",
    "s": "setting modification"
}

while True:
    user = input("-")

    if user.split(" ")[0] in commandTypes.keys():
        print("Processing " + commandTypes[user.split(" ")[0]] + " ...")
    else:
        print('ERROR [ 1 ] "' + user.split(" ")[0] + '" is not a valid command type.')
