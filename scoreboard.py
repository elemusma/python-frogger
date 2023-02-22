FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.starting_score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f'Level: {self.starting_score}', move=False, align="left", font=FONT)

    
    def increase_score(self):
        self.clear()
        self.starting_score += 1
        self.write(f'Level: {self.starting_score}', move=False, align="left", font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over!', move=False, align="center", font=FONT)