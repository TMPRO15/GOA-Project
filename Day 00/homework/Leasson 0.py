from turtle import*
#we want to paint a house

#step 1:  draw a square
shape("turtle")
speed(20)
width(5)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door

forward(70)
left(90)
color("brown")
begin_fill()
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a windows
color("cyan")
penup()
goto(60,130)
begin_fill()
left(90)
pendown()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(140,130)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick()