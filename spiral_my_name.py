#печатает цветную спираль из имени пользователя

import turtle #установка графики turtel
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

#запрос имени пользователя с помощью всплывающего окна
your_name = turtle.textinput("Введите свое имя",
                             "Как тебя зовут?")
#Нарисовать на экране спираль из имени, 100 раз

for x in range (100):
    t.pencolor (colors [x % 4]) #По очереди выбрать все 4 цвета
    t.penup
    t.forward (x*4)
    t.pendown
    t.write (your_name, font = ("Arial", int((x+4)/4), "bold"))
    t.left (92)