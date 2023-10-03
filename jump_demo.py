from turtle import forward, left, right, exitonclick

def step(size):
    forward(size)
    left(90)
    forward(size)
    right(90)

for size in range(20, 70, 5):
    step(size)

exitonclick()