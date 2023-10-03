from turtle import forward, left, right, exitonclick

def jump(height = 20):
    left(60)
    forward(height)
    right(120)
    forward(height)
    left(60)

for size in range(20, 70, 5):
    forward(30)
    jump(size)

exitonclick()