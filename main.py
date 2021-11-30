import msvcrt
import os
from colors import Color as c
from content import Content
#import pandas as pd
 
def main():
    content = []
    content.append(Content("vara 1", ["info 1", "info 2", "info 3"]))
    content.append(Content("vara 12", ["2info 1", "2info 2", "2info 3"]))
    content.append(Content("vara 123", ["3info 1", "3info 2", "3info 3"]))
    content.append(Content("vara 1234", ["4info 1", "4info 2", "4info 3"]))
    content.append(Content("vara 12345", ["5info 1", "5info 2", "5info 3"]))
    menu(content)
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
 
            case "b'\\r'":
                contentInfo(content[selectedcontent])

            case "b'q'":
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

        print(selectedcontent.info[0] + c.default)

        for i in range(1, len(selectedcontent.info)):
            print(" " * 30, end="")
            if selectedinfo == i:
                print(c.selected, end="")

            print(selectedcontent.info[i] + c.default)

        print(c.black)
        keypressed = str(msvcrt.getch())
        match(keypressed):
 
            case "b'w'" | "b'H'":
                if selectedinfo <= 0:
                    selectedinfo = len(selectedcontent.info) - 1
 
                else:
                    selectedinfo -= 1
 
            case "b's'" | "b'P'":
 
                if selectedinfo >= len(selectedcontent.info) - 1:
                    selectedinfo = 0
                else:
                    selectedinfo += 1
 
            case "b'\\r'":
                pass

            case "b'q'":
                loop = False
    
 
 
       
Clear = lambda: os.system('cls')
 
 
 
 
if __name__ == '__main__':
    main()
