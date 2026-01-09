#-----Not-----#
#Bu bir çalışmadır
#Tuple içindeki listleri başına tuple(Liste) Gibi yazın
#Durum = "njasdıjasıd" bile olsa bu bir durumdur ne yazarsak nası belirlersek o olur

import random#random komutlarını çalıstır
def harita_ciz(satir, sutun, konum, durum, hazineler):
    for i in range(satir):#satır = kançsa okadar yaz
        for j in range(sutun):#sutun = kaçsa okadar yaz


            if i == konum[0] and j == konum[1]:
                print(konum_texture, end=" ")#konum texturesini yani emojiyi çizme


            elif (i, j) == tuple(hazineler) and durum == "kaybetti":
                print(hazine_texture, end=" ") #harita texturesini yani emojiyi çizme


            elif (i, j) and durum == "kazandı":
                print(kazanma_texture, end=" ")

            #-----Kazandı Kazanmadı Devam kontrolleri ve çizimi-----#
            else:
                if durum == "devam":
                    print(harita_texture, end=" ")
                elif durum == "kaybetti":
                    print(kaybetme_texture, end=" ")

        print()#Haritayı alta doğru satırlı yapar bu olmazsa harita bozulur
durum = "devam"
konum_texture = "🙎‍♂️" #konuma emoji vermek
harita_texture = "⚪"#haritaya emoji vermek
hazine_texture = "💎"#hazineye texture vermek
kazanma_texture = "💎"
kaybetme_texture = "💩"
#-----Değişken Kontrolleri-----#
sayac = 0#deneme sayısı
isim = "Oyuncu"


satir = 4# satir 60 olursa 60xsutunluk harita bile olur
sutun = 4# sutun 100 olursa 100xsatirtlik harita bile olur


konum =[2,2]

#----- Hazine Oluşturma -----#

# hazineyi rastgele belirleme üstte aynı
hazineler = [random.randint(0, satir - 1), random.randint (0, sutun- 1)]

dolular = []
dolular.append((konum[0], konum[1]))
#----- Karışmaması için gerekli kontroller-----#
while tuple(hazineler) in dolular:
    hazineler = [random.randint(0, satir - 1), random.randint (0, sutun- 1)]
dolular.append([hazineler])

#-----Ana döngü-----#
harita_ciz(satir, sutun, konum, durum, hazineler)
while True:
    print("\nHarita")
    hareket = input(f"\n(Sistem):W/A/S/D\n({isim}):->").upper()
    if hareket == "W" and konum[0] > 0:#haritadan çıkılmasın diye > 0:
        konum[0] -=1             #bütün ifler buyüzden biraz biraz aynı
        sayac +=1
    elif hareket == "S" and konum[0] < satir - 1:
        konum[0] +=1
        sayac +=1
    elif hareket == "A" and konum[1] > 0:
        konum[1] -=1
        sayac +=1
    elif hareket == "D" and konum [1] < sutun - 1:
        konum[1] +=1
        sayac +=1
    print(f"\n(Sistem): deneme sayın:{sayac}")
    harita_ciz(satir, sutun, konum, durum, hazineler) #EN ALTA ÇİZİLMESZSE ESKİ KONUM GÖZÜKÜR HATA ÖNLEME
    #-----Oyunu kaybetti-----#
    if sayac == 10:
        print("Oyunu kaybettin")
        durum = "kaybetti"
        #Hazinenin konumunu Öğrenmek için breaktan önce harita_ciz
        harita_ciz(satir, sutun, konum, durum, hazineler)
        break
    #-----Oyunu Kazandı-----#
    if tuple(hazineler) == tuple(konum):#Oyuncu Hazinenin üzerine gelince.
        print("\n(Sistem):Oyunu kazandın.")
        durum = "kazandı"
        harita_ciz(satir, sutun, konum, durum, hazineler)
        break