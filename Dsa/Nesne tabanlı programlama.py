class Araba:
    tekerlek=0
    renk=""

    def Firla(self):
        print("vınn !")
        pass
#Burada sınıf tanımları bitti
tosba=Araba()
tosba.Firla()
class Araba:
    tekerlek = 0
    renk = "mavi"
    def TekerlekSayısı(self):
        print("Tekerlek sayısı=",self.tekerlek)
        print(self.renk)
###
tosba = Araba()
tosba.tekerlek = 5
tosba.renk = "kırmızı"
tosba.TekerlekSayısı()
print("--------------------")
kamyon = Araba()
kamyon.renk = "sarı"
kamyon.TekerlekSayısı()