import subprocess
import time
import os
from subprocess import check_output

f=open("111.ikbeneencalibbestand", "w")
f.close()

p = check_output("git status", shell=False).decode()
p = p.split("\t")
i = 0
t = 0
while t == 0:
    if p[i] == "111.ikbeneencalibbestand\n":
        t = i
    i = i+1

FileArray = []
t = t+1
while t < len(p):
    FileArray.append((p[t]).split("\n")[0])
    t = t+1
os.remove("111.ikbeneencalibbestand")

i=0
while i < len(FileArray):
    check_output("git add "+FileArray[i], shell=True).decode()
    i = i+1

check_output('git commit -m "Updated by UpGit"', shell=True).decode()

check_output('git push', shell=True).decode()
