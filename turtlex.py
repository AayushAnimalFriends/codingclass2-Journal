import turtle

smart = turtle.Turtle()

def turtle():
    while True:
        direction = input("Enter a function ie f b or turn r l or ci or u or co or up down or help")
        if (direction == "f"):
            number = int(input("Enter the number of pixels"))
            smart.forward(number)
        if (direction == "b"):
            number = int(input("Enter the number of pixels"))
            smart.back(number)
        if (direction == "r"):
            number = int(input("Enter the number of pixels"))
            smart.right(number)
        if (direction == "l"):
            number = int(input("Enter the number of pixels"))
            smart.left(number)
        if (direction == "ci"):
            number = int(input("Enter the radius"))
            smart.circle(number)
        if (direction == "u"):
            smart.undo()
        if (direction == "co"):
            number = input("Enter the color")
            smart.pencolor(number)
        if (direction == "up"):
            smart.penup()
        if (direction == "down"):
            smart.pendown()
        if (direction == "help"):
            print("f forward b back r turnright, l turnleft, ci makecircle, u undo, co color, up  drawdisabled can still move, down drawenabled")
    return
turtle()
    
    
