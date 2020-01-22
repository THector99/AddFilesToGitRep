import subprocess
import time
import os
from subprocess import check_output

f=open("111.ikbeneencalibbestand", "w")
f.close()

p = check_output("git status", shell=True).decode()
p = p.split("\t")
i = 0
t = 0
OnlyOne = False
p[len(p)-1] = p[len(p)-1].split("no")[0]
while t == 0:
    if p[i] == "111.ikbeneencalibbestand\n\n":
        OnlyOne = True
        break
    elif p[i] == "111.ikbeneencalibbestand\n":
        t = i
    
    i = i+1
if OnlyOne == False:
    FileArray = []
    t = t+1
    while t < len(p):
        FileArray.append((p[t]).split("\n")[0])
        t = t+1

    i=0
    while i < len(FileArray):
        check_output("git add "+FileArray[i], shell=True).decode()
        i = i+1

    check_output('git commit -m "Updated by UpGit made by Tim Dons"', shell=True).decode()

    check_output('git push', shell=True).decode()
os.remove("111.ikbeneencalibbestand")

p = check_output("git status", shell=True).decode()
p = p.split("\t")
endRM = False
endUP = False
i = 1
o = []
while (endRM == False or endUP==False) and i < len(p):
    print(1)
    try:
        if p[i][0] == "d" and p[i][1] == "e" and p[i][2] == "l":
            o = ((p[i]).split(" "))[4].split("\n")
            check_output("git rm -r " + o[0], shell=True).decode()
            if len(o) == 3:
                endRM = True
    except:
        print("Failed in deleting file: "+ o[0] + " or it has already been added to the delete task")

    try:
        if p[i][0] == "m" and p[i][1] == "o" and p[i][2] == "d":
            o = ((p[i]).split(" "))[3].split("\n")
            check_output("git add " + o[0], shell=True).decode()
            if len(o) == 3:
                endUP = True
            
    except:
        print("Failed in updating file: "+o[0]+" or it has already been added to the commit task")
        
    i = i +1
if len(o)>0:
    check_output('git commit -m "Update by UpGit made by Tim Dons"', shell=True).decode()
    check_output('git push', shell=True).decode()

print("Done... Press ENTER to close")
input()
