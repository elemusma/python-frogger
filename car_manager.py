COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

# class CarManager():
#     def __init__(self) -> None:
#         self.random_x = random.randrange(-280, 280)
#         self.random_y = random.randrange(-250, 250)

#     def create_car(self, random_x, random_y):
#         self.car = Turtle()
#         self.car.shape('square')
#         self.car.penup()
#         self.car.setx(random_x)
#         self.car.sety(random_y)
#         self.car.setheading(180)
#         self.car.shapesize(stretch_wid=1, stretch_len=2)
#         self.car.color(COLORS[random.randrange(len(COLORS)-1)])

#     def move(self):
#         self.car.forward(20)
#         print(self.car)

class CarManager(Turtle):
    def __init__(self, set_x_param, set_y_param, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible,)
        self.start_speed = 0.1
        self.move_increment = MOVE_INCREMENT
        self.shape('square')
        self.penup()
        self.setx(set_x_param)
        self.sety(set_y_param)
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randrange(len(COLORS)-1)])


    def move(self):
        self.forward(self.move_increment)

    
    def increase_speed(self):
        self.move_increment += 10
        print(self.move_increment)