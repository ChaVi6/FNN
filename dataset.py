from turtle import *
import random
from PIL import Image


d = {2: 'circle', 3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon', 7: 'heptagon'}

#Генерация датасета

def generate(tur1, a, b, c, c1):
    if a != 2:
        for n in range(a):
            tur1.forward(c)
            tur1.left(360.0 / a)
    else:
        tur1.circle(c)

    tur1.penup()
    tur1.goto(-(c + 10), -(c + 10))
    tur1.pendown()

    if b != 2:
        for j in range(b):
            tur1.forward(c1)
            tur1.left(360.0 / b)
    else:
        tur1.circle(c1)


for i in range(0, 1000):
    a1 = random.randint(2, 7)
    b1 = random.randint(2, 7)
    while b1 == a1:
        b1 = random.randint(2, 7)
    c = random.randint(10, 30)
    c1 = random.randint(10, 30)
    tur2 = Turtle()
    tur2.color('red')
    tur2.width(3)
    tur2.speed(0)
    tur2.hideturtle()
    screen1 = Screen()
    screen1.setup(200, 200)
    if (i % 3) == 0:
        screen1.bgpic('C:/FNN/b1.png')
    if (i % 3) == 1:
        screen1.bgpic('C:/FNN/b2.png')
    if (i % 3) == 2:
        screen1.bgpic('C:/FNN/b3.png')
    generate(tur2, a1, b1, c, c1)
    screen = tur2.getscreen()
    canvas = screen.getcanvas()
    filename = d[a1] + "_" + d[b1] + "_" + str(i)
    canvas.postscript(file=filename + ".eps")
    img = Image.open(filename + ".eps")
    img.save("C:/FNN/dataset/" + filename + ".png")
    tur2.clear()

