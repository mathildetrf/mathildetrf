from turtle import forward, left, right, exitonclick

def jump(height = 20):
    left(60)
    forward(height)
    right(120)
    forward(height)
    left(60)
    forward(height)


for size in range(20, 70, 5):
    jump()

exitonclick()