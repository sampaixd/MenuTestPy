import msvcrt
import os
import sys
from colors import Color as c
from content import Content
from time import sleep
#import pandas as pd
 
def main():
    content = []
    content.append(Content("vara 1", ["info 1", "info 2", "info 3"]))
    content.append(Content("vara 12", ["2info 1", "2info 2", "2info 3"]))
    content.append(Content("vara 123", ["3info 1", "3info 2", "3info 3"]))
    content.append(Content("vara 1234", ["4info 1", "4info 2", "4info 3"]))
    content.append(Content("vara 12345", ["5info 1", "5info 2", "5info 3"]))
    functions = [Purchase, HandleData, Exit]
    title = "Welcome to mathem autobuyer 1.0!"
    menucontent = ["Purchase wares", "Handle data", "Exit application"]

    menuUI(title, menucontent, functions, content)
    print("Closing application...")
 
 
 
def menu(content):
    loop = True
    infoContent = False
    selectedcontent = 0
    while loop:
        Clear() 
        for i in range(len(content)):
            if selectedcontent == i:
                print(c.selected, end="")
            print(content[i].name + c.default, end="")
            if len(content[selectedcontent].info) > i:
                print(" " * (30 - len(content[i].name)) + "{}".format(content[selectedcontent].info[i]))
            else:
                print()
 
        print(c.black)
        keypressed = str(msvcrt.getch())
        match(keypressed):
 
            case "b'w'" | "b'H'":
                if selectedcontent <= 0:
                    selectedcontent = len(content) - 1
 
                else:
                    selectedcontent -= 1
 
            case "b's'" | "b'P'":
 
                if selectedcontent >= len(content) - 1:
                    selectedcontent = 0
                else:
                    selectedcontent += 1
 
            case "b'\\r'" | "b'd'":
                contentInfo(content[selectedcontent])

            case "b'q'" | "b'a'":
                loop = False
        #print(keypressed)
            


def contentInfo(selectedcontent):
    loop = True
    selectedinfo = 0
    while loop:
        Clear()
        print(selectedcontent.name, end ="")
        print(" " * (30 - len(selectedcontent.name)), end="")

        if selectedinfo == 0:
            print(c.selected, end="")

        print("Add" + c.default)
        print(" " * 30, end="")
        if selectedinfo == 1:
            print(c.selected, end="")
        print("Back" + c.default)

        for i in range(len(selectedcontent.info)):
            print(" " * 30, end="")
            if selectedinfo == i + 2:
                print(c.selected, end="")

            print(selectedcontent.info[i] + c.default)

        print(c.black)
        keypressed = str(msvcrt.getch())
        match(keypressed):
 
            case "b'w'" | "b'H'":
                if selectedinfo <= 0:
                    selectedinfo = len(selectedcontent.info) + 1
 
                else:
                    selectedinfo -= 1
 
            case "b's'" | "b'P'":
 
                if selectedinfo >= len(selectedcontent.info) + 1:
                    selectedinfo = 0
                else:
                    selectedinfo += 1
 
            case "b'\\r'" | "b'd'":
                if selectedinfo == 0:
                    addInfo(selectedcontent)
                elif selectedinfo == 1:
                    loop = False
                else:
                    changeInfo(selectedcontent, (selectedinfo - 2))

            case "b'q'" | "b'a'":
                loop = False

#called when changing name of info
def addInfo(selectedcontent):
    newinfo = input("Please enter the new info: ")
    selectedcontent.info.append(newinfo)
    print("New info added, returning to menu...")
    sleep(1)

#when changing name/deleting a specified info
def changeInfo(selectedcontent, selectedinfo):  
    loop = True
    selectedchange = 0
    while loop:
        Clear()
        try:
            print(selectedcontent.name + " " * (30 - len(selectedcontent.name)) + 
            selectedcontent.info[selectedinfo] + " " * (20 - len(selectedcontent.info[selectedinfo])), end="")
            if selectedchange == 0:
                print(c.selected, end="")
            print("Back" + c.default)
            print(" " * 50, end="")
            if selectedchange == 1:
                print(c.selected, end="")
            print("Edit" + c.default)
            print(" " * 50, end="")
            if selectedchange == 2:
                print(c.selected, end="")
            print("Delete", c.default)
            
            print(c.black)
            keypressed = str(msvcrt.getch())
            match(keypressed):
                case "b'w'" | "b'H'" :
                    if selectedchange <= 0:
                        selectedchange = 2
                    else:
                        selectedchange -= 1
                case  "b's'" | "b'P'":
                    if selectedchange >= 2:
                        selectedchange = 0
                    else:
                        selectedchange += 1
                case "b'q'" | "b'a'":
                    loop = False

                case "b'\\r'" | "b'd'":
                    if selectedchange == 0:
                        loop = False
                    elif selectedchange == 1:
                        newinfo = input("Please enter the new info: ")
                        selectedcontent.info[selectedinfo] = newinfo
                        print("Info updated!")
                        sleep(1)
                    else:
                        selectedcontent.info.pop(selectedinfo)
                        loop = False
        except:
            #print("No info in content, returning to prevoius menu...")
            #sleep(1)
            loop = False
#test code, imports def into another def as a list
###############################################################
def Purchase(content):
    print("purchasing products...")

def HandleData(content):
    menu(content)
def Exit(content):
    sys.exit()

functions = [Purchase, HandleData, Exit]
title = "Welcome to mathem autobuyer 1.0!"
content = ["Purchase wares", "Handle data", "Exit application"]

def menuUI(title, content, functions, data):
    prevcontentspaces = 0
    selected = 0
    loop = True
    while loop:
        print(title)
        print()
        for i in range(len(content)):
            if selected == i:
                print(c.selected, end="")
            print(content[i] + c.default)
        print(c.black)
        pressedkey = str(msvcrt.getch())
        print(c.default)
        Clear()
        match(pressedkey):
                case "b'w'" | "b'H'" :
                    if selected <= 0:
                        selected = len(content) - 1
                    else:
                        selected -= 1
                case  "b's'" | "b'P'":
                    if selected >= len(content) - 1:
                        selected = 0
                    else:
                        selected += 1
                case "b'q'" | "b'a'":
                    loop = False

                case "b'\\r'" | "b'd'":
                    functions[selected](data)
#####################################################################


       
Clear = lambda: os.system('cls')
 
 
 
 
if __name__ == '__main__':
    main()
    #menuUI(title, content, functions)
