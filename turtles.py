import turtle
import time
import random

HEIGHT,WIDTH = 400,500
COLORS = ["red", "green", "blue", "black", "cyan", "orange", "pink", "yellow", "purple", "brown"]

def get_racers():
	while True:
		racers = 0
		racers = input("Enter the no. of racers: ")
		if racers.isdigit():
			racers = int(racers)
		else:
			print("Value entered is not numeric... Try again!")
			continue

		if 2 <= racers <=10:
			return racers
		else:
			print("Value entered is not between 2-10... Try again!")


def create_turtles(colors):
	turtles = [] 
	space = WIDTH // (len(colors)+1)
	for i,color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i+1) * space, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)
	return turtles

def init_race():
	screen = turtle.Screen()
	screen.setup(WIDTH,HEIGHT)
	screen.title("Turtles racing!!")

def race():
	racers = get_racers()
	colors = COLORS[:racers]
	init_race()
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1,20)
			racer.forward(distance)

			x,y  = racer.pos()
			if y >= HEIGHT//2 - 10:
				return colors[turtles.index(racer)]

winner = race()
print("The winnner of the race is: ",winner)



