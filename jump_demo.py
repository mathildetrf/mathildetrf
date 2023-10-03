from turtle import forward, left, right, exitonclick

def jump(size):
    left(60)
    forward(size)
    right(120)
    forward(size)
    left(60)


for size in range(20, 70, 5):
    jump(size)

exitonclick()