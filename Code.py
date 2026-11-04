import math
import turtle
from random import *

width = turtle.window_width()
height = turtle.window_height()

turtle.speed(10000)

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

def draw_waves(largeur=width, hauteur=height):
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.pencolor("blue")
    while turtle.xcor() < (largeur/2):
        turtle.circle(5, 180)
        turtle.circle(-5, 180)
    turtle.setheading(180) # bas
    turtle.goto(turtle.xcor(), -(width/2))
    turtle.setheading(180) # gauche
    turtle.forward(largeur)
    turtle.right(90)
    turtle.forward(hauteur/10)
    turtle.end_fill()
        
def seine():
    turtle.penup()
    turtle.goto(-(width/2), -(height/2))
    turtle.pendown()
    draw_wall(width, height/8, 20, 10, "brown", "black")
    turtle.setheading(90) # haut
    turtle.forward(height/12)
    turtle.setheading(-90) # droite
    draw_waves(width, height/12)
    
def draw_wall(x, y, brick_x=20, brick_y=10, fill="brown", couleur="black"):
    position = turtle.position()
    rectangle(x, y, fill, couleur)
    for i in range(0, int(y/brick_y)+1):
        if i % 2 == 0: # pour alterner entre les briques décalées 1 fois sur deux
            turtle.forward(brick_x/2)
            for j in range(0, int(x/brick_x)-1):
                rectangle(brick_x, brick_y, fill, couleur)
                turtle.forward(brick_x)
        else:
            for j in range(0, int(x/brick_x)):
                rectangle(brick_x, brick_y, fill, couleur)
                turtle.forward(brick_x)
                
        turtle.up()
        turtle.goto(position)
        turtle.down()
        turtle.left(90)
        turtle.forward(brick_y * i)
        turtle.right(90)
    turtle.goto(position)

def route():
    turtle.penup()
    turtle.goto(-(width/2), -(height/2))
    turtle.pendown()
    rectangle(width, height/8, "gray", "black")
    turtle.setheading(90) # haut
    turtle.forward(height/16)
    turtle.setheading(0) # droite
    
    # dessiner les lignes blanches de la route
    while turtle.xcor() < (width/2):
        turtle.pencolor("white")
        turtle.width(height/50)
        turtle.forward(width/10)
        turtle.penup()
        turtle.forward(width/20)
        turtle.pendown()
        
    turtle.pencolor("black")
    turtle.width(1)
    turtle.penup()
    turtle.goto(-(width/2), -(height/2))
    turtle.pendown()
    
def draw_ground():
    environement = ["seine", "herbe", "route"]
    environement_choisi = random.choice(environement)
    if environement_choisi == "seine":
        seine()
    elif environement_choisi == "herbe":
        herbe()
    elif environement_choisi == "route":
        route()
                
def car(x, fill="red", couleur="black"):
    angle = 45
    y = x/4
    turtle.pencolor(couleur)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y*(4/5))
    turtle.circle(y/5, 90)
    turtle.forward(x/5)
    turtle.right(angle)
    turtle.forward((y/1.5) / math.sin(math.radians(angle)))
    turtle.left(angle)
    turtle.forward(x/3)
    turtle.left(90)
    turtle.forward((y/1.5))
    turtle.right(90)
    turtle.forward(x/4)
    turtle.left(90)
    turtle.forward(y)
    turtle.end_fill()

car(100, "red", "black")

def test_fonction():
    seine()
    #route()
    turtle.goto(0, 0)
    turtle.setheading(0) # droite
    rectangle(150, 100, "red")
    triangle(150, 100, "green")
    fenetre(100, 100, light_blue)
    # draw_wall(200, 100, 20, 10, "brown", "black")

# seine()
test_fonction()

# fin du code
# permet à le fenètre de rester fermé
turtle.done()