# ----Yılan oyunu----#
import random


def harita_ciz(satir, sutun, yilan_konum, elmalar):
    for i in range(satir):
        for j in range(sutun):
            if i == yilan_konum[0] and j == yilan_konum[1]:
                print(yilan_konum_texture, end=" ")
            elif (i, j) in elmalar:
                print(elma_texture, end=" ")
            else:
                print(harita_texture, end=" ")
        print()


# ----değişkenler----#
# ----Textures----#
yilan_konum_texture = "🐍"
elma_texture = "🍎"
harita_texture = "🟫"
# ----Değişkenler----#
satir = 3
sutun = 3
yilan_konum = [satir // 2, sutun // 2]
elma_1 = random.randint
elma_sayaci = 0
# ----Listeler----#
dolular = []
dolular.append(tuple(yilan_konum))
elmalar = [
    (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
    (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
    (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
    (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
    (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
]
# -----İç içe girmeme kontrol döngüleri-----#


while elmalar in dolular:
    elmalar = [
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
    ]
    dolular.append(elmalar)
while elmalar in elmalar:
    elmalar = [
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
        (random.randint(0, satir - 1), random.randint(0, sutun - 1)),
    ]
    dolular.append(elmalar)

# -----Ana Döngü-----#
harita_ciz(satir, sutun, yilan_konum, elmalar)

while True:
    # -----Kullanıcıdan yürüme komudu alma ve büyük harfe çevirme-----#
    hareket = input("\n(Sistem):W/A/S/D\n(Oyuncu):->").upper()

    # -----Kullanıcı konumunu güncelleme-----#
    if hareket == "W" and yilan_konum[0] > 0:
        yilan_konum[0] -= 1
    elif hareket == "S" and yilan_konum[0] < satir - 1:
        yilan_konum[0] += 1
    elif hareket == "A" and yilan_konum[1] > 0:
        yilan_konum[1] -= 1
    elif hareket == "D" and yilan_konum[1] < sutun - 1:
        yilan_konum[1] += 1
    elif hareket == "Q":
        break
    else:
        print("Yanlış tuş/yön")
    # -----Elmaları yeme kontrolü-----#
    if tuple(yilan_konum) in elmalar:
        elmalar.remove((tuple(yilan_konum)))
        elma_sayaci += 1
        print(f"\n(Sistem): Puan: {(elma_sayaci)}")
    harita_ciz(satir, sutun, yilan_konum, elmalar)

# yılan mesela 3, 4 konumunda
# elmayı 4, 4 konumunda yılan yer
# yılanın son konumu 2 -> elmadaki konuma yılanın başını ekle, önceki konum kalsın
#                    ı--> elma yendikten sonra yılanın bir sonraki hareketi yılanın boyunu bir uzatır
