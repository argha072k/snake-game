import turtle
import random
import time

delay=0.1
score=0
highestscore=0

#for snake body
bodies=[]

#for screen
s=turtle.Screen()
s.title("snake game")
s.bgcolor("blue")
s.setup(width=600,height=600)
s.tracer(0)

#snake head
head=turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="Stop"

#for snake food
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

#for scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
		font=("candara", 24, "bold"))

#giving directions

def moveup():
    if head.direction!="down":
        head.direction="up"

def movedown():        
    if head.direction!="up":
        head.direction="down"

def moveright():        
    if head.direction!="left":
        head.direction="right"

def moveleft():        
    if head.direction!="right":
        head.direction="left" 


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)      

#user events
s.listen()
s.onkeypress(moveup,"w")
s.onkeypress(movedown,"s")
s.onkeypress(moveleft,"a")
s.onkeypress(moveright,"d")

#gameplay

while True:
	s.update()
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		for body in bodies:
			body.goto(1000, 1000)
		bodies.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, highestscore), align="center", font=("candara", 24, "bold"))
	if head.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding body
		new_body = turtle.Turtle()
		new_body.speed(0)
		new_body.shape("square")
		new_body.color("orange") 
		new_body.penup()
		bodies.append(new_body)
		delay -= 0.001
		score += 20
		if score > highestscore:
			highestscore = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, highestscore), align="center", font=("candara", 24, "bold"))

	# Checking for head collisions with bodies
	for index in range(len(bodies)-1, 0, -1):
		x = bodies[index-1].xcor()
		y = bodies[index-1].ycor()
		bodies[index].goto(x, y)
	if len(bodies) > 0:
		x = head.xcor()
		y = head.ycor()
		bodies[0].goto(x, y)
	move()

    #for snake collision with itself
	for body in bodies:
		if body.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for body in bodies:
				body.goto(1000, 1000)
			body.clear()

    #update new score
			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(
				score, highestscore), align="center", font=("candara", 24, "bold"))
	time.sleep(delay)

s.mainloop()





