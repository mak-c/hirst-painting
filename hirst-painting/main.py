import turtle
import random
artist = turtle.Turtle()
turtle.colormode(255)

color_list = [(181, 5, 51), (45, 177, 51), (242, 135, 54), (53, 18, 66), (215, 113, 156), (2, 115, 171), (248, 193, 47), (144, 39, 102), (2, 83, 77), (78, 43, 42)]


def draw_dot():
    artist.speed(0)
    artist.dot(20, random.choice(color_list))


artist.penup()
artist.hideturtle()
starting_y = -400
for x in range(10):
    artist.setposition(-400, starting_y)
    for i in range(10):
        draw_dot()
        artist.forward(50)
    starting_y += 50


screen = turtle.Screen()
screen.exitonclick()
