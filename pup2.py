import turtle
wn = turtle.Screen()
lovelace = turtle.Turtle()
lovelace.penup()
lovelace.forward(60)
lovelace.pendown()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    lovelace.left(angle)
    lovelace.forward(100)
print("The pirate's final heading was", lovelace.heading())
wn.exitonclick()
