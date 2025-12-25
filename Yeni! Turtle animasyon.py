import turtle
import random
t = turtle.Turtle()
t.shape("arrow")
t.penup()
def rastgele_konum():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    turtle.ontimer(rastgele_konum, 1000) #1 saniye sonra hareket et
    t.write("Merhaba", font =("Arial", 16, "normal"))

rastgele_konum()
turtle.done()