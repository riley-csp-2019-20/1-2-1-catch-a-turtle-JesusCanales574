# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
turtleshape = "turtle"
trutlecolor = "green"
turtlesize = .1
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
joe = trtl.Turtle(shape = turtleshape)
joe.color(trutlecolor)
joe.shapesize(turtlesize)
joe.speed(0)


scoreboard = trtl.Turtle()
scoreboard.ht()
scoreboard.speed(0)
scoreboard.penup()
scoreboard.goto(-370,270)

font_setup = ("Arial", 30, "bold")
scoreboard.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.speed(0)
counter.goto(-270,270)
counter.ht()
counter.pendown

#-----game functions--------
def turtle_clicked(x,y): 
    print("joe got clicked")
    change_position()
    update_score()

def change_position():
    joe.penup()
    joe.ht()
    if not timer_up:
        joex = random.randint(-400,400)
        joey = random.randint(-300,300)
        joe.goto(joex,joey)
        joe.st()


def update_score():
    global score
    score += 1
    print(score)
    scoreboard.clear()
    scoreboard.write(score, font=font_setup)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over ", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 



#-----events----------------

wn = trtl.Screen()
wn.bgcolor("lightblue")
joe.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop() 