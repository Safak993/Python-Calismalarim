class Araba:
    tekerlek = 10
    renk = "Beyaz" #parametre gönderilmezse 10 tekerlekli ve beyaz renk gönderilir

    def __init__(self, rengi, tekerlek_sayisi): #init yapıcı
        self.tekerlek = tekerlek_sayisi
        self.renk = rengi
# -------------
tosba = Araba("Mavi", 5) # bu sayede tek tek yazmaya gerek kalmıyo
kamyon = Araba("Sarı",10)
print(tosba.renk , tosba.tekerlek, "\n",
    kamyon.renk, kamyon.tekerlek)