import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()




# for _ in range(100):


screen.listen()
screen.onkey(player.move, 'Up')

cars_list = []

game_is_on = True
moving_forward_speed = 10
while game_is_on:
    random_x = random.randrange(-280, 280)
    random_y = random.randrange(-230, 230)
    cars = CarManager(350, random_y)

    time.sleep(.1)
    screen.update()

    # Detect turtle reaching end of screen
    if player.ycor() > 280:
        player.restart()
        scoreboard.increase_score()
        # cars.increase_speed()
        moving_forward_speed += 10
    
    # create cars

    cars_list.append(cars)

    # keep_going = True
    # while keep_going:
    for car in range(0, len(cars_list), 3):
        new_car = cars_list[car]
        
        new_car.forward(moving_forward_speed)
        # print(f'Cars movement increment: {cars.move_increment}')

        if player.distance(new_car) < 20:
            # i += 1
            # print(f'crash {i}')
            scoreboard.game_over()
            game_is_on = False
        
    print(cars.start_speed)
            
            # game_is_on = False
    # cars.create_car(300, random_y)
    # cars.forward(20)
    # print(cars.xcor())
    # cars.move()
    
    
screen.exitonclick()
    # Increase Level after reaching end of screen