import turtle
import random

wn = turtle.Screen() 
wn.title("Turtle") 
wn.bgcolor("lightgreen")

tim = turtle.Turtle()
ps = 1
tim.pensize(ps)

def label1():
    turtle.color('lightgreen')
    turtle.setposition(-600, 300)
    turtle.color('black')
    style = ('Courier', 20, 'italic')
    turtle.write('Press h for help.', font=style, align='left')
    turtle.hideturtle()

label1()

def up():
    tim.forward(10)

def down():
    tim.backward(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

colors = ["red", "blue", "green", "yellow", "white", "black", "lightgreen"]

def clickLeft(x, y):
    tim.color(random.choice(colors))

def clickRight(x, y):
    tim.stamp()

def help():
    wn.bgcolor("black")
    turtle.color('black')
    style = ('Courier', 20, 'italic')
    style1 = ('Courier', 12, 'italic')
    style2 = ('Courier', 30, 'italic')
    turtle.setposition(0, 0)
    turtle.color('white')
    turtle.write('''**Press up arrow to move forward & down arrow to move backward** \n
          **Press left and right arrow to change angle**''', font=style1, align='center')
    turtle.color('black')
    turtle.setposition(0, -40)
    turtle.color('white')
    turtle.write('Press p to increse pensize.', font=style, align='center')
    turtle.color('black')
    turtle.setposition(0, -80)
    turtle.color('white')
    turtle.write('Press m to decrese pensize.', font=style, align='center')
    turtle.color('black')
    turtle.setposition(0, -120)
    turtle.color('white')
    turtle.write('Press u to undo.', font=style, align='center')
    turtle.color('black')
    turtle.setposition(0, -160)
    turtle.color('white')
    turtle.write('Right click mouse to change color.', font=style, align='center')
    turtle.color('black')
    turtle.setposition(0, -200)
    turtle.color('white')
    turtle.write('Left click mouse to stamp.', font=style, align='center')
    turtle.color('black')
    turtle.setposition(0, -250)
    turtle.color('white')
    turtle.write('Press q to quit help.', font=style2, align='center')

def quit_help():
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.hideturtle()
    wn.bgcolor("lightgreen")
    label1()

def increse_ps():
    global ps
    ps += 1
    tim.pensize(ps)

def decrese_ps():
    global ps
    ps -= 1
    tim.pensize(ps)

def undo():
    tim.undo()

wn.listen()

turtle.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRight, 3) # 3: Right Mouse Button
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(quit_help, "q")
wn.onkey(help, "h")
wn.onkey(increse_ps, "p")
wn.onkey(decrese_ps, "m")
wn.onkey(undo, "u")

wn.mainloop()
