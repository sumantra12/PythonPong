#By: Sumantra Das
#HARVARD ID: 41487461
#Start: July 2, 2020
#End: August 6, 2020

"""
About this Program:

This is a simple Pong game created on Python
using the build-in turtle module. This the first
game I created with the features of sound, when
the ball collides with the users paddles or the wall.
The style of code is more functional based. Other
features include, a motion ball and two paddles
that users may control, as a two player game and
a score system. 

"""

import turtle
import os

#sets up the turtle screen as the varible userinterface
userinterface = turtle.Screen()

#the title of the application
userinterface.title("Classic Pong")

#background color is set
userinterface.bgcolor("#c55454")

#the size of the window
userinterface.setup(width = 800, height = 600)
userinterface.tracer(0)


### GAME PROPERTIES ######

# batter 1

#sets batter 1 as a turtle 
batter_1 = turtle.Turtle()

#animation speed is one
batter_1.speed(0)

#sets it as a square, with stretch 5 and lenght as 1
batter_1.shapesize(stretch_wid=5, stretch_len = 1)
batter_1.shape("square")

#color of batter one is red
batter_1.color("red")

#starts are -350 on the game window
batter_1.penup()
batter_1.goto(-350, 0)



# batter 2

#set as turtle, with sqaure shape
batter_2 = turtle.Turtle()
batter_2.speed(0)
batter_2.shapesize(stretch_wid=5, stretch_len = 1)
batter_2.shape("square")

#green colored batter to distinguish between player 1 & 2
batter_2.color("green")

#starts are 350 on the game window
batter_2.penup()
batter_2.goto(350, 0)



#ball

#Set to turtle and animation speed of zero
userball = turtle.Turtle()
userball.speed(0)

#shape is black sqaure
userball.shape("square")
userball.color("black")

#starts at 0,0(center) and moves 2 pixels at x direction and -2 y direction 
userball.penup()
userball.goto(0, 0)
userball.dx = 2
userball.dy = -2

#score interface
playersscore = turtle.Turtle()
playersscore.speed(0)
playersscore.color("blue")

#hides turtle, due to no motion
playersscore.penup()
playersscore.hideturtle()

#Design and placement of scoreboard 
playersscore.goto(0, 260)
playersscore.write("Player A: 0   Player B: 0", font=("Times", 25, "normal"), align="center")



#tracking scores
score_1 = 0
score_2 = 0


# Moving the batter for 1 up and down the screen 
def batter_1_movup():
    mov1 = batter_1.ycor()
    mov1 += 18
    batter_1.sety(mov1)
    
def batter_1_movdown():
    mov2 = batter_1.ycor() 
    mov2 -= 18
    batter_1.sety(mov2)

#moving the batter for 2 up and down the screen 
def batter_2_movup():
    mov1 = batter_2.ycor()
    mov1 += 18
    batter_2.sety(mov1)
    
def batter_2_movdown():
    mov2 = batter_2.ycor() 
    mov2 -= 18
    batter_2.sety(mov2)



# add your keyboard binding for batter a and b
#move player 1 with w and s & player 2 with i and k
userinterface.listen()
userinterface.onkeypress(batter_1_movdown, "s")
userinterface.onkeypress(batter_1_movup, "w")
userinterface.onkeypress(batter_2_movup, "i")
userinterface.onkeypress(batter_2_movdown, "k")



###### MAIN GAME LOOP #######

while True:
    
    #updates the userinterface with the movement and score tracking
    userinterface.update()
    
    #moving the the ball
    userball.setx(userball.xcor() + userball.dx)
    userball.sety(userball.ycor() + userball.dy)
    
    #when ball collides with top border, sound plays
    if userball.ycor() > 290:
        userball.sety(290)
        userball.dy = userball.dy * -1
        os.system("afplay bounce.wav&")
    
    #when ball collides with bottom border, sound plays
    if userball.ycor() < -290:
        userball.sety(-290)
        userball.dy = userball.dy * -1
        os.system("afplay bounce.wav&")
        
    #returns to centre after passing the batter for player 2
    if userball.xcor() > 390:
        userball.goto(0, 0)
        userball.dx = userball.dx * -1
        
        #score is incremented and updated for player 1
        score_1 = score_1 + 1
        os.system("afplay score.wav&")
        playersscore.clear()
        playersscore.write("Player A: {}   Player B: {}".format(score_1, score_2), font=("Times", 25, "normal"), align="center")
        
        
    #returns to centre after passing the batter for player 1   
    if userball.xcor() < -390:
        userball.goto(0, 0)
        userball.dx = userball.dx * -1
        
        #score is incremented and updated for player 2
        score_2 = score_2 + 1
        os.system("afplay score.wav&")
        playersscore.clear()
        playersscore.write("Player A: {}   Player B: {}".format(score_1, score_2), font=("Times", 25, "normal"), align="center")
        
        
    #ball and user batter collision
    if userball.xcor() > 340  and (userball.ycor() < batter_2.ycor() + 41 and userball.ycor() > batter_2.ycor() -52):
        
        #bounces the ball back to the opponenet user
        userball.dx = userball.dx * -1.05
        userball.setx(340)
        os.system("afplay bounce.wav&")
    
    if userball.xcor() < -340  and (userball.ycor() < batter_1.ycor() + 41 and userball.ycor() > batter_1.ycor() -52):
        userball.dx = userball.dx * -1.05
        userball.setx(-340)
        os.system("afplay bounce.wav&")