import turtle
import time

veri = turtle.Screen()
veri.title("Renk Seçimi")

# Turtle oluştur (mesajları göstermek için)
mesaj_t = turtle.Turtle()
mesaj_t.hideturtle()
mesaj_t.penup()
mesaj_t.goto(0, 50)  # ekranın üst kısmına yazı yaz

# Renkleri tanımla
renkler = ["red", "blue", "yellow"]
renk = None

while not renk:
    girilen = veri.textinput("Renk Seçimi", "Renginizi yazın: kırmızı/mavi/sarı")

    if not girilen:  # boş veya iptal
        mesaj_t.clear()
        mesaj_t.write("Hiçbir şey girmediniz!", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)
        continue
    if girilen == "çık":
        exit(

        )

    # Türkçe → İngilizce çevir
    if girilen.lower() == "kırmızı":
        girilen = "red"
    elif girilen.lower() == "mavi":
        girilen = "blue"
    elif girilen.lower() == "sarı":
        girilen = "yellow"

    if girilen not in renkler:
        mesaj_t.clear()
        mesaj_t.write("Yanlış renk girdiniz! Tekrar deneyin.", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)
        continue

    renk = girilen
    mesaj_t.clear()  # doğru renk girildiğinde mesajı temizle

# Turtle oluştur ve seçilen rengi uygula
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.color(renk)
t.goto(0, -1)
t.write(f"Turtle rengi: {renk}", align="center", font=("Arial", 20, "normal"))

turtle.done()
