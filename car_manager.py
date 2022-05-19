from turtle import Turtle
import random
COLORS = ['red','orange','yellow','green','blue','purple']
STRT_MOVE_DIS = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.allcars=[]
        self.carspd = STRT_MOVE_DIS
    def createcar(self):
        rc = random.randint(1,6)
        if rc == 1:
            nc = Turtle()
            nc.shape('square')
            nc.shapesize(stretch_wid=1,stretch_len=2)
            nc.color(random.choice(COLORS))
            nc.penup()
            nc.goto(280,random.randint(-240,240))
            self.allcars.append(nc)
    def mov(self):
        for car in self.allcars:
            car.backward(self.carspd)
    def level_up(self):
        self.carspd+=MOVE_INCREMENT