#Fonksiyon öğreniyorum
#Küçük Çalışmalar
#def return anahtar kelimeler
#parametrelere varsayılan değerler atmak
# def bilgi_ver(): #def anahtar kelimesi olduğu sürece python bilgi_ver() i fonksiyon olarak anladı
#     print("İşlem başarılı.") #bilgi_ver() komudunu yazınca bu printi yazar


    # tam olarakyukarısı yani bu yazı bloğun içindedir bloğun içinde olduğu sürece çalışır komutlar
# bilgi_ver() #5kez yazarsak beşkez yazar
# bilgi_ver()                  #ayrıca printte değiştirdiğimiz sayı veya harflerde aynı şekilde otomatik olarak bilgi_ver' e atanır
# bilgi_ver()
# bilgi_ver()
# bilgi_ver()
#################################
#################################
#######/Parametre ekleme\#########
##################################
##################################
# def carp(x,y): #x ve y bir parametre carp fonksiyonu kullanıldığında gözükür
#     print(f"x * y = {x * y}")#eğer carp (3,6) ise başka bir parametre eklersek örn : y eklersek hata verir parametreyi atamamız lazım
# carp(3,6)

########/Liste alan fonksiyon\########
# def ortalama_hesapla(liste):
#     toplam = sum(liste)
#     adet = len(liste)
#     ortalama = toplam / adet
#     print(f"Girilen sayıların ortalaması{ortalama}")
# ortalama_hesapla([1,2,3,4,5,6,7])#girilen sayıların ortalamaları
#######################################################################
# def buyuk_harfe_cevir(metin):
#     metin = metin.upper()#girilen metni büyük harfe çevirme
#     print(metin)
# buyuk_harfe_cevir("AnSyTyyp")#çalıştırılınca burda yazılan şey büyük harfe çevrildi

# def selamla(mesaj,isim):
#     print(f"{mesaj} {isim}.")#ilk mesajı gosterme sonrada girilen ismi yazıp. yazması
# selamla("Merhaba","Ali")#ilk yazılan merhaba {mesaj} ikinci yazılanda isim şeysine atandı

######/Parametrelere varsayılan atama######
# def selamla(mesaj,isim = "anonim"):#isim = "anonim" girilmeyen isim yerine geçen yazı
#     print(f"{mesaj} {isim}.")
# selamla("merhaba ") #bu şekilde çalışırsa atanmamış isim fonksiyonu anonim olarak yazılacak
# selamla("merhaba","Berat")#isme atanan berat olduğu için sadece berat yazar anonim kaybolur


# def indirim_yap(fiyat,yuzde = 20):#birşey girmediğim zaman yüzdeyi 20 kabul et
#     indirim_miktarı = fiyat * (yuzde / 100)
#     indirimli_fiyat = fiyat - indirim_miktarı
#     print(f"İndirimli tutar: {indirimli_fiyat}")
# indirim_yap(50,10)#yuzde yazıldı  = 20 kayboldu = 10 olarak ayarlandı
# indirim_yap(50)#paranteze yuzde eklemedik yukarıdaki yuzde = 20 çalıştı

def topla(x,y):
    print(x + y)
topla(3,8)