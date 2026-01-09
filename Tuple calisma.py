import random

def harita_ciz(satir, sutun, agac, konum, hazine):
    for i in range(satir):
        for j in range(sutun):
            if (i, j) == konum:
                print("X", end=" ")

sutun = 5
satir = 5
dolular = []

hazine_satir = random.randint(0, satir - 1)
hazine_sutun = random.randint(0, sutun - 1)

agac = random.randint(0, satir - sutun)
konum = (satir // 2, sutun // 2)
hazine = (random.randint(0, satir - 1), random.randint(0, sutun - 1))
dolular.append((konum[0], konum[1]))

while ([hazine_satir, hazine_sutun]) in dolular : # hazine tekrar rastgele konumlandırılıyor
    hazine_satir = random.randint(0, satir - 1)
    hazine_sutun = random.randint(0, sutun - 1)

dolular.append((hazine_satir, hazine_sutun)) # dolular listesine hazine konumu ekleniyor

while (agac in dolular): # ağaç tekrar rastgele konumlandırılıyor
    agac = (random.randint(0, satir - 1), random.randint(0, sutun - 1))

dolular.append(agac) # dolular listesine ağaç konumu ekleniyor

print(dolular)
print()