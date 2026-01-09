# test
# print("döngü")
d = 20
a = 5


def miracin_printi(text):
    print(text)


# print("\nDöngü ve fonksiyon\n")
# sayi_listesi(d)

# print("\nelle\n")
# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# print("******")
# print("*******")
# print("********")
# print("*********")
# print("**********")
# print("***********")
# print("************")
# print("*************")
# print("**************")

# print("\nDöngü ile\n")
# for i in range(d):
#     print(i * "*")

# print(
#     "\n------------------------------------------------------------------------------\n"
# )
# print("\nDöngü ile\n")
# for i in range(d):
#     print(i * "*")


# print("\nelle\n")
# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# print("******")
# print("*******")
# print("********")
# print("*********")
# print("**********")
# print("***********")
# print("************")
# print("*************")
# print("**************")


# sayi_listesi(d)


def aptal_print(text):
    print("yazmicam 😡😡")


def zeki_print(isim):
    print(f"Merhaba {isim}, nasılsın?\n")
    print("Ben senin kim olduğunu az önce öğrendim.\n")
    print("Seninle tanıştığıma memnun oldum")


# print(
#     "\n------------------------------------------------------------------------------\n"
# )

# miracin_printi("mirac")

# print("mirac")

# aptal_print("mirac")

# zeki_print("mirac")


def sayi_listesi(turSayisi):
    for i in range(turSayisi):
        print(i * "*")


# satir sutun oyuncu

# satir, sutun, oyuncu = 10, 10, [5, 8]
10, 10, [5, 7]
#    [0,1,2,3,4,5,6,7,8,9]
#     1 2 3 4 5 6 7 8 9 10
# 1   * * * * * * * * * *
# 2   * * * * * * * * * *
# 3   * * * * * * * * * *
# 4   * * * * * * * * * *
# 5   * * * * * * * * * *
# 6   * * * * * * * * * *
# 7   * * * * * * * * * *
# 8   * * * * * * * * * *
# 9   * * * * * X * * * *
# 10  * * * * * * * * * *

#  elif satır == 1 and sutun == 2:
#  oyuncu[1, 2]

# print(oyuncu[0])
# print(oyuncu[1])


# def konumlariGoster(satir, sutun):
#     for i in range(satir):
#         for j in range(sutun):
#             print(f"[{i},{j}]", end=" ")
#         print("\n")

import random
import time
print("\n(Safak993):Bu oyunu safak993 yaptı bilgine")
time.sleep(1)
print("\n(Safak993): Sadece 30 hakkın var Bol şans İyi eğlenceler😊")

print("\n(Sistem):Bilgilendirme ağaca değersen en başa gelirsin.\nGizli Zombiye değersen 5hakkın gider.")
isim = input("\n(Sistem):Oyuna başlamak için isminizi giriniz.\n(Kullanıcı):->")
if not isim.isalpha():
    print("\n(Sistem):Böyle bir isim yok(Doğru giriniz.)")
    print("\n(Sistem):Oyun sonlandırılıyor...")
    time.sleep(1.5)
    exit()
else:
    print("\n(Sistem):Oyun Hazırlanıyor...")
time.sleep(1.5)
print("\n(Sistem):Oyun kodları yazılıyor...")
time.sleep(1)
print("(Sistem):Oyun başlıyor")
time.sleep(0.5)
def harita_ciz(satir, sutun, konum, agac, agac2, zombi_1, zombi_2):
    for i in range(satir):
        for j in range(sutun):
            if i == konum[0] and j == konum[1]:
                print("X", end=" ")
            elif (i, j) == agac:
                print("🌲", end=" ")
            elif (i, j) == agac2:
                print("🌲", end=" ")
            else:
                print("*", end=" ")
        print()


satir = 5
sutun = 10
sayac = 0
konum = [2,4]
hazine_satir = random.randint(0, satir - 1)
hazine_sutun = random.randint(0, sutun - 1)
zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
zombi_2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
zombiler = [zombi_1, zombi_2]
while zombi_1 == zombi_2:
    zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while zombi_1 == (hazine_satir, hazine_sutun) or zombi_2 == (hazine_satir, hazine_sutun):
    zombi_1 = random.randint(0, satir - 1)  #zombi ile hazine aynı yerde olamaz
    zombi_2 = random.randint(0, sutun - 1)
while zombi_1 == konum or zombi_2 == konum:
    zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun -1)
    zombi_2 = random.randint(0, satir - 1), random.randint(0, sutun -1)
agac = random.randint(0, satir - 1), random.randint(0, sutun - 1)
agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while agac == agac2:#Ağaçlar aynı konumda olamaz
    agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while agac == (hazine_satir, hazine_sutun) or agac2 == (hazine_satir, hazine_sutun):
    agac = random.randint(0, satir - 1)#agac ile  hazine konumu aynı olamaz
    agac2 = random.randint(0, sutun - 1)
while agac == konum or agac2 == konum:
    agac = random.randint(0, satir - 1), random.randint(0, sutun - 1)
    agac2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while hazine_satir == konum[0] and hazine_sutun == konum[1]:#Safak993: eğer hazine konumu oyuncu ile aynı ise yeniden belirler
    hazine_satir = random.randint(0, satir - 1)#hazine konumu aynı olamaz
    hazine_sutun = random.randint(0, sutun - 1)
while zombi_1 == agac or zombi_1 == agac2 or zombi_2 == agac or zombi_2 == agac2:
    zombi_1 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
    zombi_2 = random.randint(0, satir - 1), random.randint(0, sutun - 1)
while True:
    print("\nHarita")
    harita_ciz(satir, sutun, konum, agac, agac2, zombi_1, zombi_2)
    hareket = input(f"\n(Sistem):Hareket (W/A/S/D)Kapamak Q\n({isim}):-> ").upper()
    if hareket == "W" and  konum[0] > 0:
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
        time.sleep(1)
        print("Oyundan çıkılıyor...")
        time.sleep(0.5)
        break
    if (konum[0], konum[1]) == agac or (konum[0], konum[1]) == agac2:
        print("\n (Sistem):Ağaca çarptınız! başlangıca yeniden gidiyosunuz😒.")
        konum = [2,4]
    if tuple(konum) in zombiler:#ilkkez tuple kullandım :D
        print(f"\n(Sistem):👹👹 Gizli zombiye dokundun 5hakkın gitti!")
        sayac +=5
        print(f"(Sistem):Kalan hak:{sayac}")
        zombiler.remove(tuple(konum))
    if konum[0] == hazine_satir and konum[1] == hazine_sutun:
        print("🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇 ")
        print("\n(Sistem):Tebrikler! Hazineyi buldunuz!")
        break
    print(f"(Sistem):Şuana kadar {sayac} hareket yaptınız.")
    if sayac >= 30:
        print("\n(Sistem):30 hamle yaptınız, oyunu kaybettiniz😒")
        break