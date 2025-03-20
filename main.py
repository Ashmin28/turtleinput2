import random
import turtle

screen = turtle.Screen()
screen.setup(750, 750)
screen.bgcolor("black")

t = turtle.Turtle()

# menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("Background Colors",font=("arial",30,"normal"),align="center")
t.penup()

t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(-75,50)
t.pendown()
t.pencolor("Azure")
t.write("2. Azure",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(-75,0)
t.pendown()
t.pencolor("Aquamarine")
t.write("3. Aquamarine",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(-75,-50)
t.pendown()
t.pencolor("darkkhaki")
t.write("4. DarkKhaki",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Choose a Color",font=("arial",30,"normal"),align="center")
t.penup()


choose = int(input("Choose a Color: "))
if choose == 1:
    screen.bgcolor("Tan")
elif choose == 2:
    screen.bgcolor("Azure")
elif choose == 3:
    screen.bgcolor("Aquamarine")
elif choose == 4:
    screen.bgcolor("Darkkhaki")
t.clear()

name = input("Enter your name: ")


operation = random.randint(1,4)

if operation == 1:
    symbol = "+"
    # add
    num1 = random.randint(-100,100)
    num2 = random.randint(-100, 100)
    solution = num1 + num2
elif operation == 2:
    symbol = "-"
    # subtract
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    solution = num1 - num2
elif operation == 3:
    # multiply
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    solution = num1 * num2
elif operation == 4:
    # divide
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    sign = random.randint(1,2)
    if sign == 2:
        num2 = -1+num2


t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("Blue")
t.write(name,font=("arial",30,"normal"),align="center")
t.penup()

t.goto(-200,0)
t.pendown()
t.pencolor("green")
t.write(num1,font=("arial",30,"normal"),align="center")
t.penup()

t.goto(-100,0)
t.pendown()
t.pencolor("red")
t.write("+",font=("arial",30,"normal"),align="center")
t.penup()

t.goto(0,0)
t.pendown()
t.pencolor("hot pink")
t.write(num2,font=("arial",30,"normal"),align="center")
t.penup()

t.goto(100,0)
t.pendown()
t.pencolor("orange")
t.write("=",font=("arial",30,"normal"),align="center")
t.penup()

ans = int(input("Enter your Answer: "))

t.goto(200,0)
t.pendown()
t.pencolor("purple")
t.write(sum,font=("arial",30,"normal"),align="center")
t.penup()

t.goto(0,-100)
t.pendown()
t.pencolor("purple")
t.write("Your answered: " + str(ans),font=("arial",30,"normal"),align="center")
t.penup()

if ans == sum:
    screen.bgcolor("dodgerblue")
    t.goto(0, 50)
    t.pencolor("green")
    t.write("Your answer is CORRECT", font=("arial", 30, "normal"), align="center")
else:
    screen.bgcolor("red")
    t.goto(0, 50)
    t.pencolor("darkred")

    t.write("Your answer is WRONG", font=("arial", 30, "normal"), align="center")





#LAST LINE OF CODE!!!
turtle.done()