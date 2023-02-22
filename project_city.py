from turtle import *
from random import *

Screen().setup(400, 400)
speed(0)
Screen().bgcolor("darkBlue")

for i in range(100): # рисуем звездное небо
    x = randint(-200, 200)
    y = randint(-200, 200)
    penup()
    goto(x, y)
    dot(randint(1, 5), "yellow")

def square(l, m): # функция рисуем окно
    penup()
    goto(l, m)
    pendown()
    fillcolor("yellow")
    begin_fill()
    forward(10)
    left(90)
    for i in range(3):
        forward(20)
        left(90)
    forward(10)
    end_fill()


penup()
goto(-200, 0)
pendown()
fillcolor("blue")
begin_fill()

mydict = {}
lst_y = []
k = -200
h = 0
i = 1
while k < 200: #рисуем город и заносим координаты вершин в словарь, чтобы окна при использовании random были ниже крыши дома
    if i % 2 == 1:
        y = h
        x = randint(k + 30, k + 50)
        mydict.setdefault(y, []).append(x)
        goto(x, y)
        k = x
        print(pos(), x)

    if i % 2 == 0:
        x = k
        y = randint(-100, 150)
        while y in lst_y:
            y = randint(-100, 150)
        lst_y.append(y)
        goto(x, y)
        h = y
        mydict.setdefault(y, []).append(x)
        print(pos(), y)
    i += 1

goto(k, -200)
goto(-200, -200)
goto(-200, 0)
end_fill()

mydict.setdefault(0, []).append(-200)

f = -200
while f < 180:  # рисуем окна:
    xw = randint(f, f + 50)
    f = xw + 10
    for k, v in mydict.items():
        s, s1 = mydict[k]
        if s < xw < s1:
            ch1 = [40, 80, 120]
            m = k - (choice(ch1))  # k - макс значение y
            l = s + ((s1 - s) / 2)  # значнеие x
            square(l, m)

