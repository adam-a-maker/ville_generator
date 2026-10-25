import turtle
from random import *

height=500
width=500

# edit this line to control where window appears
turtle.setup(width, height, startx=-1, starty=0)

# Variables globales
light_blue = "#9CD6E9"

# Fonctions
def rectangle(x, y, fill="white", couleur="black"):
    turtle.pencolor(couleur)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
    turtle.end_fill()
    
def triangle(x, y, fill="white", couleur="black"):
    turtle.pencolor(couleur)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(x)
        turtle.left(120)
    turtle.end_fill()
    
def fenetre(x, y, color):
    rectangle(x, y, "black")
    if x > y:
        X = x/2 -y*(5/100)
        Y = y/2 -y*(5/100)
    else:
        X = x/2 -x*(5/100)
        Y = y/2 -x*(5/100)
    
    for _ in range(0, 2):
        rectangle(X, Y, color)
        turtle.forward(x)
        turtle.left(90)
        rectangle(Y, X, color)
        turtle.forward(y)
        turtle.left(90)

def seine():
    turtle.penup()
    turtle.goto(-(width/2), -(height/2))
    turtle.pendown()
    rectangle(width, height/5, "gray")
    
    
seine()


def draw_ground():
    environement = [seine, herbe, ville, route, sable]
    environement_choisi = random.choice(environement)
    if environement_choisi == seine:
        seine()
    elif environement_choisi == herbe:
        herbe()
    elif environement_choisi == ville:
        ville()
    elif environement_choisi == route:
        route()
    elif environement_choisi == sable:
        sable()
                
def test_fonction():
    rectangle(150, 100, "red")
    triangle(150, 100, "green")
    fenetre(10, 10, light_blue)

test_fonction()

# fin du code
# permet à le fenètre de rester fermé
turtle.done()