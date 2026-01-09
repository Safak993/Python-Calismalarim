import turtle
import random
wn = turtle.Screen()
wn.title("Turtle çalısma safak")
girilen = wn.textinput("devammı" "çıkmı?:", ":")
if girilen == "çık":
    exit()
else:
    t = turtle.Turtle()
    t.shape("turtle")
    # t.penup()

    def rastgele_konum():
         x = random.randint(-200, 200)
         y = random.randint(-200, 200)
         t.goto(x, y)
         turtle.ontimer(rastgele_konum, 100)
    rastgele_konum()
    turtle.done()