import turtle

pen = turtle.Turtle()

def draw_structure():
	pen.goto(-250, 0)
	pen.forward(50)
	pen.left(60)

def draw_handle():
	pen.forward(50)
	pen.right(40)
	pen.forward(10)
	pen.backward(20)
	pen.forward(10)
	pen.right(140)
	pen.forward(200)

def draw_wheel():
	pen.circle(50)
	pen.left(90)
	pen.forward(50)
	for i in range(10):
		pen.forward(50)
		pen.backward(50)
		pen.right(36)

pen.left(50)
draw_handle()
draw_wheel()

turtle.done()