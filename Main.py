import turtle

turtle.Screen().bgcolor("beige")
sc = turtle.Screen()
sc.setup(400 , 300)

turtle.title("Welcome To Turtle")

board = turtle.Turtle()


for i in range(6):
    board.forward(70)
    board.right(60)



turtle.done()
