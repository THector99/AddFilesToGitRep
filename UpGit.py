from pynput.keyboard import Key, Controller
import time
import os

keyboard = Controller()
Path = __file__ #the path file of the file
Path = Path[:-8]
fileNames = []
print("type done to continue or give an ENTER")
while True:
    fileName = input("Give the filename: ")
    if fileName == "done" or fileName == "":
        break
    else:
        fileNames.append(fileName)

print(fileNames)
YN = input("Are these the right files? Y/N (standard Y):")
if YN == "n" or YN == "N":
    exit()
	
com = 'updated by UpGit.py - THector99 github'
print("standard commit comment: " + com)
YN = input("Do you want to apply a custom commit comment? Y/N (standard N):")

if YN == "Y" or YN == "y":
        com = input("custom commit: ")

time.sleep(.100)
    
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

time.sleep(.100)
keyboard.type("git pull")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

i=0
while i < len(fileNames):
    keyboard.type("git add " + fileNames[i])
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    i = i + 1

time.sleep(.100)

keyboard.type('git commit -m ' + '"' + com + '"')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)

keyboard.type('git push')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

#time.sleep(5)
#
#time.sleep(.100)
#keyboard.press(Key.alt)
#keyboard.press(Key.tab)
#
#keyboard.release(Key.alt)
#keyboard.release(Key.tab)
#time.sleep(.100)
#comment the next session out if you use heroku or change the git push heroku to something you want to push to other than your own master branch
#YN = input("Do you want to push to heroku master branch? Y/N: ")
#
#if YN == "Y" or YN == "y":
#        time.sleep(.100)
#        keyboard.press(Key.alt)
#        keyboard.press(Key.tab)
#
#        keyboard.release(Key.alt)
#        keyboard.release(Key.tab)
#        time.sleep(.100)
#        keyboard.type('git push heroku master')
#        keyboard.press(Key.enter)
#        keyboard.release(Key.enter)
#