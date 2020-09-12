import turtle #imports the turtle
from dataclasses import dataclass #imports classes 
smart = turtle.Turtle() #creating the turtle
def Getsequence(): #defining the function
    global Point        #allowing our class to be used outside the function
    n = 1 #creating our variable
    @dataclass #creating the class from here
    class Point:
        cmd: str
        value: int t# to here
    ListOfNumbers = []# creating the list we will return 
    while True:
        direction = input("Enter a function ie f b or turn r l or ci or co or up down") #getting the input 
        if (direction == "f"): #checking if the  previos input was f
            number = int(input("Enter the number of pixels")) #giving another input
            p = Point('f',number) #usig our class to set create a variable that is a class 
            ListOfNumbers.append(p) #putting that variable into the eturn output of commands given all the other if statements are basically the same
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
        finish = input("would you like to enter another command") # continue or not continue
        if (finish == 'n'): #checking if they said don't contiune
            return ListOfNumbers #ending the function and returning our list of commands
        if (finish == 'no'):
            return ListOfNumbers


def loop(Getsequence): #defining a function with a parameter which is for the previous function
    global n  #globaling n outside of function this is used for redo n is the list of commands
    n = Getsequence #creating n
    times = int(input("how many times do you want to repeat you can repeat once")) #input to ask how many times to repeat the program
    for y in range(0, times): #repeating the program the desired amount of times
        for i in range(0, len(n)): #used to identify which element in the list you want
            direction = n[i].cmd #ok this looks comlex we are defining a variable then in the listofcommands or n we are checking the ith element from for i in range in the previous line and then inside of that the cmd is telling it which one we want the value or command
            if (direction == "f"): #Checking if direction from the previous line is f
                number = n[i].value #this looks complex too but its almpost the same as direction except we are using value
                smart.forward(number)# using the imfo from direction and number we finaly run the turtle command all other if statements are almost the same            
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
    return len(n)*times #used for the undo loop command we need to know how many times to undo basically these 2 are just the 2 things at the end of the for loops
        



print("help: f is forward b is backward r is right l is left ci is circle co is color up is disable draw/pen up down is enable draw/pendown when doing redo it will ask you how many times you want to repeat")
while True: #INfinity loop
    a = input("would you like to undo (u) or redo (r) or create a new loop (CNL)") #asking to choose between running the previous function undo or redo
    if (a == 'CNL'): 
        b = loop(Getsequence()) #running the loop but putting it into a variable for undo
    if (a == 'u'):
        c = input(" would you like to undo one action(O) or the whole previous loop (W)") #asking to choose between once or whole loop
        if (c == 'O'):
            smart.undo()
        if (c == 'W'):
            for i in range(0, b):
                smart.undo()
    if (a == 'r'):
        b = loop(n)
    
    

    
    
