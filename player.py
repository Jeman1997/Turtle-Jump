from turtle import Turtle
STRT_POS=(0,-280)
MOVE_DIS=10
FIN_LINE_Y=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STRT_POS)
        self.setheading(90)
    def go_up(self):
        self.fd(MOVE_DIS)
    def go_dn(self):
        self.backward(MOVE_DIS)
    def gostrt(self):
        self.goto(STRT_POS)
    def finline(self):
        if self.ycor()>280:
            return True
        else:
            return False