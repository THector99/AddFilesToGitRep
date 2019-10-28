from pynput.keyboard import Key, Controller
import time
import os

keyboard = Controller()
Path = __file__ #the path file of the file
Path = Path[:-8]
fileNames = []
print("type done om verder te gaan")
while True:
    fileName = input("Geef de bestandsnaam: ")
    if fileName != "done":
        fileNames.append(fileName)
    else:
        break

print(fileNames)
YN = input("Zijn dit de juiste bestanden? Y/N: ")
if YN == "n" or YN == "N":
    exit()
    
keyboard.press(Key.cmd)
keyboard.press('r')

keyboard.release('r')
keyboard.release(Key.cmd)

time.sleep(.100)

keyboard.type("cmd")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(.200)
keyboard.type("cd "+Path)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
i=0
while i < len(fileNames):
    keyboard.type("git add " + fileNames[i])
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    i = i + 1

time.sleep(.100)

keyboard.press(Key.alt)
keyboard.press(Key.tab)

keyboard.release(Key.alt)
keyboard.release(Key.tab)

time.sleep(.100)

com = 'updatet by UpGit.py - THector99 github'
YN = input("Do you want to apply a custom commit? Y/N: ")

if YN == "Y" or YN == "y":
	com = input("custom commit: ")

time.sleep(.100)

keyboard.press(Key.alt)
keyboard.press(Key.tab)

keyboard.release(Key.alt)
keyboard.release(Key.tab)

time.sleep(.100)

keyboard.type('git commit -m ' + '"' + com + '"')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)

keyboard.type('git push')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5)

time.sleep(.100)
keyboard.press(Key.alt)
keyboard.press(Key.tab)

keyboard.release(Key.alt)
keyboard.release(Key.tab)
time.sleep(.100)

YN = input("Do you want to push to heroku master branch? Y/N: ")

if YN == "Y" or YN == "y":
	time.sleep(.100)
	keyboard.press(Key.alt)
	keyboard.press(Key.tab)

	keyboard.release(Key.alt)
	keyboard.release(Key.tab)
	time.sleep(.100)
	keyboard.type('git push heroku master')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)