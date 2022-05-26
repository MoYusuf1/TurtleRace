from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)

mike = Turtle()
raph = Turtle()
leo = Turtle()
don = Turtle()
fifth = Turtle()
sixth = Turtle()


def enter_mike():
    mike.shape("turtle")
    mike.color("orange")
    mike.penup()
    mike.goto(-150, 120)


def enter_raph():
    raph.shape("turtle")
    raph.color("red")
    raph.penup()
    raph.goto(-150, 80)


def enter_leo():
    leo.shape("turtle")
    leo.color("blue")
    leo.penup()
    leo.goto(-150, 40)


def enter_don():
    don.shape("turtle")
    don.color("purple")
    don.penup()
    don.goto(-150, 0)


def enter_fifth():
    fifth.shape("turtle")
    fifth.color("brown")
    fifth.penup()
    fifth.goto(-150, -40)


def enter_sixth():
    sixth.shape("turtle")
    sixth.penup()
    sixth.goto(-150, -80)
    sixth.color("green")


def enter_racers():
    enter_mike()
    enter_raph()
    enter_leo()
    enter_don()
    enter_fifth()
    enter_sixth()


def move():
    don.forward(random.randrange(1, 10))
    if don.xcor() > 250:
        return 1
    mike.forward(random.randrange(1, 10))
    if mike.xcor() > 250:
        return 2
    leo.forward(random.randrange(1, 10))
    if leo.xcor() > 250:
        return 3
    raph.forward(random.randrange(1, 10))
    if raph.xcor() > 250:
        return 4
    fifth.forward(random.randrange(1, 10))
    if fifth.xcor() > 250:
        return 5
    sixth.forward(random.randrange(1, 10))
    if sixth.xcor() > 250:
        return 6


def race(distance):
    for racer in range(1, distance):
        if move() == 1:
            print("Contestant #1 Don won the race!")
            return 1
        elif move() == 2:
            print("Contestant #2 Mike won the race!")
            return 2
        elif move() == 3:
            print("Contestant #3 Leo won the race!")
            return 3
        elif move() == 4:
            print("Contestant #4 Raph won the race!")
            return 4
        elif move() == 5:
            print("Contestant #5 Fifth won the race!")
            return 5
        elif move() == 6:
            print("Contestant #6 Sixth won the race")
            return 6


enter_racers()

bet = screen.textinput("Wager", "Make your bet below! (enter contestant number)")
if bet == race(1000):
    print("You win a million dollars")
else:
    print("Your out of luck. Hand over your money *snatches it from your hand*")

screen.exitonclick()
