import turtle

# List of colors for drawing
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

# Create turtle object
t = turtle.Pen()
turtle.bgcolor('black')

# Draw colorful spiral pattern
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()