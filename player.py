from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color('green')
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)


    def restart(self):
        self.goto(STARTING_POSITION)
