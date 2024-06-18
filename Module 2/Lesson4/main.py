import os
import time
from pynput import keyboard 
def clean():
    print('\033[2J\033[H')

scene = []

def clean(sleepTime):
    
    time.sleep(sleepTime)
    print('\033[2J\033[H')
def cleanScene():
    scene.clear()
    

def printTriangle(height, xOffset, yOffset, ch):
    widthDown = 2 * (height - 1) + 1
    printChar("\n",yOffset)
    for i in range(height):
        width = 2 * i + 1
        printChar(" ", xOffset)
        space = int((widthDown - width) / 2)
        printChar(" ", space)
        for k in range(width):
            if k != 0 and k != width-1 and i != height-1:
                printChar(ch, 1)
            else:
                printChar("#", 1)
        printChar(" ", space)
        printChar("\n", 1)

def printChar(ch, i):
    for j in range(i):
        scene.append(ch)



xPos = 0
yPos = 0
size = 1
print("Use WASD to Move Use QE to grow")
def Input(xPos, yPos, size):
    
    with keyboard.Events() as events:
        event = events.get(1e6)
        key = event.key.char
    if key == 'w':
        yPos-=1
    elif key == 's':
        yPos+=1
    elif key == 'a':
        xPos-=1
    elif key == 'd':
        xPos +=1

    if key == 'q':
        size-=1
    elif key == 'e':
        size+=1
    if xPos < 0:
        xPos = 0
    if yPos < 0:
        yPos = 0
    if size < 1:
        size = 1
    return xPos, yPos, size
def printSquare(xx,yy,xOffset,yOffset,character):
    for _ in range(yOffset):
        print()

    def printEnd():
        print(" "*xOffset+"#"*xx)
    def printRow():
        print(" "*xOffset+"#"+character*(xx-2)+"#")

    printEnd()
    for _ in range(yy-2):
        printRow()
    printEnd()
while True:
    xPos, yPos,  size = Input(xPos=xPos, yPos=yPos, size=size)
    clean(0.01)
    cleanScene()
    printTriangle(size, xPos, yPos, " ")
    #printSquare(size,size, xPos,yPos+size, " ")
 
    scene.append("a")
    print(scene)
    print((''.join(scene)))



