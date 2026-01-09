import random


# import time
print("\n(Safak993):Bu oyunu safak993 👋 yaptı bilgine")
# time.sleep(1)
print("\n(Safak993): Sadece 40 hakkın var Bol şans İyi eğlenceler😊")

print(
    "\n(Sistem):Bilgilendirme ağaca değersen en başa gelirsin.\nGizli Zombiye değersen 5hakkın gider\nParayı alırsan 4hak kazanırsın.."
)
# isim = input("\n(Sistem):Oynamak için İsminizi giriniz.(Oyuncu):->")
isim = "Oyuncu"
if not isim.isalpha():
    print("\n(Sistem):Böyle bir isim yok(Doğru giriniz.)")
    print("\n(Sistem):Oyun sonlandırılıyor...")
    # time.sleep(1.5)
    exit()
else:
    print("\n(Sistem):Oyun Hazırlanıyor...")
# time.sleep(1.5)
print("\n(Sistem):Oyun kodları yazılıyor...")
# time.sleep(1)
print("(Sistem):Oyun başlıyor")
# time.sleep(0.5)


def harita_ciz(satir, sutun, konum, agaclar, paralar, hazine_konumu, oyun_durumu):
    for i in range(satir):
        for j in range(sutun):
            if i == konum[0] and j == konum[1]:
                print("👤", end=" ")
            elif (i, j) in agaclar and oyun_durumu == "devam":  # Ağaçların konumlarını kontrol et
                print(engel_texture, end=" ")
            elif (i, j) in paralar and oyun_durumu == "devam": #paraların konumları oyun bitince gidecek
                print(para_texture, end=" ")
            elif (i, j) in zombiler and oyun_durumu == "devam": #zombilerin konumları oyun bitince gitsin
                print(zombiler_texture, end=" ")
            elif (i, j) == hazine_konumu and oyun_durumu != "devam":
                print(hazine_texture, end=" ")
            else:
                if oyun_durumu == "devam":
                    print(harita_texture, end=" ")
                elif oyun_durumu == "kazandi":
                    print(kazanma_texture, end=" ")
                elif oyun_durumu == "kaybetti":
                    print(kaybetti_texture, end=" ")
                else:
                    print(harita_texture, end=" ")
        print()


# Oyun textureleri
harita_texture = "⬜️"
kazanma_texture = "🎇"
engel_texture = "🌲"
para_texture = "🎁" # "💰"
zombiler_texture = "🧟"
hazine_texture = "💎"
kaybetti_texture = "💩"
# Oyun değişkenleri
satir = 6 # harita üstten alta doğru boyutu
sutun = 6 #harita boyutu
sayac = 0  # Hareket sayacı
konum = [satir // 2, sutun // 2]  # Başlangıç konumu ortada #// tam bölme yuvarlama
para = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
para2 = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
paralar = [para, para2]
hazine_satir = random.randint(0, satir - 1)
hazine_sutun = random.randint(0, sutun - 1)
zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
zombi_2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
zombiler = [zombi_1, zombi_2]
agac = random.randint(0, satir - 1), random.randint(0, sutun - 1)
agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
agaclar = [agac, agac2]
hayalet = random.randint(0, satir - 1), random.randint(0, sutun -1)
hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
hayaletler = [hayalet, hayalet2]
durum = "devam"
dolular = []  # dolu konumları tutan liste
######################## kontroller ayrı yerde olamaz ########################
#dolular.append((konum[0], konum[1]))

#while([hazine_satir, hazine_sutun] in dolular):
    #hazine_satir = random.randint(0, satir - 1)
    #hazine_sutun = random.randint(0, sutun - 1)

#dolular.append((hazine_satir, hazine_sutun))

#while(agac in dolular):
    #agac = random.randint(0, satir - 1), random.randint(0, sutun - 1)

#dolular.append(agac)

#while(agac2 in dolular):
 #   agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)

#dolular.append(agac2)

#while(hayalet in dolular):
    #hayalet = random.randint(0, satir - 1), random.randint(0, sutun - 1)

#dolular.append(hayalet)

#while(hayalet2 in dolular):
 #   hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)

#dolular.append(hayalet2)

#while(para in dolular):
    #para = random.randint(0, satir - 1), random.randint(0, sutun - 1)

#dolular.append(para)

#while(para2 in dolular):
    #para2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)

#dolular.append(para2)

# print(dolular)

while zombi_1 == zombi_2:
    zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while zombi_1 == (hazine_satir, hazine_sutun) or zombi_2 == (
    hazine_satir,
    hazine_sutun,
):
    zombi_1 = random.randint(0, satir - 1)  # zombi ile hazine aynı yerde olamaz
    zombi_2 = random.randint(0, sutun - 1)
while zombi_1 == konum or zombi_2 == konum:
    zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
    zombi_2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while zombi_1 == agac or zombi_1 == agac2 or zombi_2 == agac or zombi_2 == agac2:
    zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
    zombi_2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)

if agac == agac2:  # Ağaçlar aynı konumda olamaz
    agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)

while agac == (hazine_satir, hazine_sutun) or agac2 == (hazine_satir, hazine_sutun):
    agac = random.randint(0, satir - 1)  # agac ile  hazine konumu aynı olamaz
    agac2 = random.randint(0, sutun - 1)
while agac == konum or agac2 == konum:
    agac = random.randint(0, satir - 1), random.randint(0, sutun - 1)
    agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while (
    hazine_satir == konum[0] and hazine_sutun == konum[1]
):  # Safak993: eğer hazine konumu oyuncu ile aynı ise yeniden belirler
    hazine_satir = random.randint(0, satir - 1)  # hazine konumu aynı olamaz
    hazine_sutun = random.randint(0, sutun - 1)
if para == para2: # paralar aynı konumda olamaz
    para2 = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
if para == agac or para == agac2 or para2 == agac or para2 == agac2: #paralar ağaçlarla aynı konumda olamaz
    para = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
    para2 = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
if para == (hazine_satir, hazine_sutun) or para2 == (hazine_satir, hazine_sutun) :#para hazineyle aynı konumda olamaz
    para = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
    para2 = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
if para == (konum[0] and konum[1]) or para2 == (konum[0] and konum[1]):#para adamla aynı olamaz
    para = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
    para2 = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
# dolular[] = [agaclar] + zombiler + [(hazine_satir, hazine_sutun)] + [konum]
# Kısa yöntem (deneysel)

# while(para in dolular):
#     para = (random.randint(0, satir - 1), random.randint(0, sutun - 1))

if hayalet == hayalet2: # hayaletler aynı konumda olamaz
    hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
if hayalet == konum or hayalet2 == konum: # hayaletler oyuncu ile aynı konumda olamaz
    hayalet = random.randint(0, satir - 1), random.randint(0, sutun -1)
    hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
if hayalet == agac or hayalet == agac2 or hayalet2 == agac or hayalet2 == agac2: # hayaletler ağaçlarla aynı konumda olamaz
    hayalet = random.randint(0, satir - 1), random.randint(0, sutun -1)
    hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
if hayalet == (hazine_satir, hazine_sutun) or hayalet2 == (hazine_satir, hazine_sutun): # hayaletler hazine ile aynı konumda olamaz
    hayalet = random.randint(0, satir - 1), random.randint(0, sutun -1)
    hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
if hayalet == zombi_1 or hayalet == zombi_2 or hayalet2 == zombi_1 or hayalet2 == zombi_2: # hayaletler zombilerle aynı konumda olamaz
    hayalet = random.randint(0, satir - 1), random.randint(0, sutun -1)
    hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
if hayalet == para or hayalet == para2 or hayalet2 == para or hayalet2 == para2: # hayaletler paralarla aynı konumda olamaz
    hayalet = random.randint(0, satir - 1), random.randint(0, sutun -1)
    hayalet2 = random.randint(0, satir - 1), random.randint(0, sutun -1)


# Ana döngü
while True:
    print("\nHarita")
    harita_ciz(satir, sutun, konum, agaclar, paralar, (hazine_satir, hazine_sutun), durum)

    if durum == "devam":
        pass
    else:
        break

    hareket = input(f"\n(Sistem):Hareket (W/A/S/D)Kapamak Q\n({isim}):-> ").upper()
    if hareket == "W" and konum[0] > 0:
        konum[0] -= 1
        sayac += 1
    elif hareket == "S" and konum[0] < satir - 1:
        konum[0] += 1
        sayac += 1
    elif hareket == "A" and konum[1] > 0:
        konum[1] -= 1
        sayac += 1
    elif hareket == "D" and konum[1] < sutun - 1:
        konum[1] += 1
        sayac += 1
    elif hareket == "Q":
        print("Oyun Kodları Siliniyor...")
        # time.sleep(1)
        print("Oyundan çıkılıyor...")
        # time.sleep(0.5)
        break
    if (konum[0], konum[1]) == agaclar[0] or (konum[0], konum[1]) == agaclar[1]:
        print("\n (Sistem):Ağaca çarptınız! başlangıca yeniden gidiyosunuz😒.")
        konum = [int(satir / 2), int(sutun / 2)]
    if tuple(konum) in zombiler:  # ilkkez tuple kullandım :D
        print(f"\n(Sistem):🧟 Zombiye dokundun seni ıssırdı 5 hakkın gitti! 🧟")
        sayac += 5
        print(f"(Sistem):Kalan hak:{sayac}")
        zombiler.remove(tuple(konum))
    if tuple(konum) in paralar: #ilkkez tuple kullandım
        print("Parayı aldınız 4hak kazandınızz!")
        sayac -=4
        paralar.remove(tuple(konum))
    if tuple(konum) in hayaletler:
        print("\n(Sistem):👻Hayaleti buldun seni ıssırdıııııı👻 3hak gitti")
        sayac +=3
        hayaletler.remove(tuple(konum))
    if konum[0] == hazine_satir and konum[1] == hazine_sutun:
        print("\n(Sistem):Tebrikler! Hazineyi buldunuz!")
        durum = "kazandi"
    print(f"(Sistem):Şuana kadar {sayac} hareket yaptınız.")
    if sayac >= 40:
        print("\n(Sistem):40 hamle yaptınız, oyunu kaybettiniz😒")
        durum = "kaybetti"
# 💰eklenecek dokununca 4 hak gelecek