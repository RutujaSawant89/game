import turtle
import time
import random
from playsound import playsound 

def left():
    global moveship
    moveship = -4 
     
def right():
    global moveship
    moveship = 4
    
def space():
    global bullet
    global spaceship
    
    if bullet.isvisible()== False:
        playsound('sound.mp3',False)
        bullet.setpos(spaceship.xcor(),spaceship.ycor()+70)
        bullet.showturtle()

def makeEnemies():
    e=None
    enemies=[]
    for x in range(1,6):
        e=turtle.Turtle()
        e.hideturtle()
        e.shape('enemy.gif')
        e.penup()
        e.setpos(random.randint(-350,350),int(300*x))
        e.showturtle()
        enemies.append(e)
        
    return enemies

def dist(value1, value2):
    if(value1>value2):    
        return value1-value2
    else:
        return value2-value1 

    
win=turtle.Screen()
win.setup(800,600)
win.title("spaceblaster")
win.bgpic("space.gif")
win.tracer(0)

turtle.register_shape('ship.gif')
turtle.register_shape('bulle.gif')
turtle.register_shape('enemy.gif')
turtle.register_shape('explosion.gif')
spaceship = turtle.Turtle()
spaceship.shape('ship.gif')
spaceship.penup()
spaceship.setpos(0,-200)
spaceship.speed(0)

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape('bulle.gif')
bullet.penup()

en = makeEnemies()

turtle.listen()
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(space,"space")


moveship=0
points =0
remain=len(en)

score =turtle.Turtle()
score.hideturtle()
score.pencolor("yellow")
score.penup()
score.setpos(375,250)
score.write(f"score:{points}",align="right", font=("arial",20,"bold"))


while remain > 0:
    spaceship.setheading(0)
    spaceship.forward(moveship)
    
    if bullet.isvisible():
        bullet.setheading(90)
        bullet.forward(35)
        
    if bullet.ycor()>(win.window_height()/2):
        bullet.hideturtle()

    if spaceship.xcor() > 325:
       moveship=0
    elif spaceship.xcor() < -500:
      moveship=0
      
    for enemy in en :
        if (enemy.ycor()> -500):
            enemy.setheading(270)
            enemy.forward(3)
            
        if(dist(enemy.xcor(),bullet.xcor()) < 35 and
           dist(enemy.ycor(),bullet.ycor()) < 50 and
           bullet.isvisible()):
             enemy.shape('explosion.gif')
             enemy.tiltangle(1)
             points= points +1
             score.clear()
             score.write(f"score:{points}",align="right",font=("arial",20,"bold"))
             

             
             
             
             
      
        
        
        if(enemy.tiltangle()>40):    
            enemy.hideturtle()
        elif(enemy.tiltangle()>0):
            enemy.tiltangle(enemy.tiltangle() + 1)
            
           
        
                
    win.update()
    time.sleep(0.002)


