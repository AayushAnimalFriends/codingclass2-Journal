import turtle
from dataclasses import dataclass
smart = turtle.Turtle()

def Getsequence():
    global Point        
    n = 1
    @dataclass
    class Point:
        cmd: str
        value: int
    ListOfNumbers = []
    while True:
        direction = input("Enter a function ie f b or turn r l or ci or co or up down")
        if (direction == "f"):
            number = int(input("Enter the number of pixels"))
            p = Point('f',number)
            ListOfNumbers.append(p)
        if (direction == "b"):
            number = int(input("Enter the number of pixels"))
            p = Point('b',number)
            ListOfNumbers.append(p)
        if (direction == "r"):
            number = int(input("Enter the number of degrees"))
            p = Point('r',number)
            ListOfNumbers.append(p)
        if (direction == "l"):
            number = int(input("Enter the number of degrees"))
            p = Point('l',number)
            ListOfNumbers.append(p)
        if (direction == "ci"):
            number = int(input("Enter the radius"))
            p = Point('ci',number)
            ListOfNumbers.append(p)
        if (direction == "co"):
            number = input("Enter the color")
            p = Point('co',number)
            ListOfNumbers.append(p)
        if (direction == "up"):
            p = Point('up',0)
            ListOfNumbers.append(p)
        if (direction == "down"):
            p = Point('down',0)
            ListOfNumbers.append(p)
        finish = input("would you like to enter another command")
        if (finish == 'n'):
            return ListOfNumbers
        if (finish == 'no'):
            return ListOfNumbers


def loop(Getsequence):
    global n
    n = Getsequence
    times = int(input("how many times do you want to repeat you can repeat once"))
    for y in range(0, times):
        for i in range(0, len(n)):
            direction = n[i].cmd
            if (direction == "f"):
                number = n[i].value
                smart.forward(number)
            if (direction == "b"):
                number = n[i].value
                smart.back(number)
            if (direction == "r"):
                number = n[i].value
                smart.right(number)
            if (direction == "l"):
                number = n[i].value
                smart.left(number)
            if (direction == "ci"):
                number = n[i].value
                smart.circle(number)
            if (direction == "co"):
                number = n[i].value
                smart.pencolor(number)
            if (direction == "up"):
                smart.penup()
            if (direction == "down"):
                smart.pendown()
    return len(n)*times
        



print("help: f is forward b is backward r is right l is left ci is circle co is color up is disable draw/pen up down is enable draw/pendown when doing redo it will ask you how many times you want to repeat")
while True:
    a = input("would you like to undo (u) or redo (r) or create a new loop (CNL)")
    if (a == 'CNL'):
        b = loop(Getsequence())
    if (a == 'u'):
        c = input(" would you like to undo one action(O) or the whole previous loop (W)")
        if (c == 'O'):
            smart.undo()
        if (c == 'W'):
            for i in range(0, b):
                smart.undo()
    if (a == 'r'):
        b = loop(n)
    
    

    
    
