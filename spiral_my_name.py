#печатает цветную спираль из имени пользователя

import turtle #установка графики turtel
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
sides = int (turtle.numinput("Сколько сторон", "Сколько сторон вы хотите (1-8)?", 4, 1, 8, ))
#запрос имени пользователя с помощью всплывающего окна
your_name = turtle.textinput("Введите свое имя",
                             "Как тебя зовут?")
#Нарисовать на экране спираль из имени, 100 раз

for x in range (360):
    t.pencolor (colors [x % sides]) #По очереди выбрать все 4 цвета
    t.forward(x * 3 / sides + x)
    t.left (360 / sides + 1)
    t.width (x * sides / 200)

    #t.penup
    #t.forward (x*4)
    #t.pendown
    #t.write (your_name, font = ("Arial", int((x+4)/4), "bold"))
    #t.left (92)