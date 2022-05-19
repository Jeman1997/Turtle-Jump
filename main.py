import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scorebd

s=Screen()
s.setup(width=600,height=600)
s.tracer(0)
s.listen()

scbd=Scorebd()

plyr=Player()
s.onkey(plyr.go_up,'Up')
s.onkey(plyr.go_dn,'Down')

carmngr = CarManager()

is_on=True
while is_on:
    time.sleep(0.1)
    s.update()
    carmngr.createcar()
    carmngr.mov()
    #collision with any car
    for c in carmngr.allcars:
        if c.distance(plyr)<15:
            is_on=False
            scbd.gmover()
    #next level
    if plyr.finline():
        plyr.gostrt()
        carmngr.level_up()
        scbd.level+=1
        scbd.updscre()
s.exitonclick()