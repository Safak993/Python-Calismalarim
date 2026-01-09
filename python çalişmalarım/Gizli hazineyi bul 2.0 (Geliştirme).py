# Not ### 19.12.2025 Yaptığım en büyük projedir(Yeniyim lütfen ön yargılı olmayınız🎈)
# 👋Selam önceki Gizli hazineyi bul projemin bir güncellemesi
# İyi eğlenceler!😊
import random

import time

print("(Safak993):Hey selam👋")
time.sleep(1.5)
print("(Safak993):Bu oyunu yapan Safak993 bilgine🎈.")
time.sleep(1)
print("(Safak993):Sadece iyi eğlenceler😊")

isim = input("\n(Sistem):Oyuna başlamak için isminizi giriniz.\n(Kullanıcı):->")
if not isim.isalpha():
    print("\n(Sistem):Böyle bir isim yok(Doğru giriniz.)")
    exit()
else:
    print("\n(Sistem):Oyun Hazırlanıyor...")
time.sleep(1.5)
print("\n(Sistem):Oyun kodları yazılıyor...")
time.sleep(1)
print("(Sistem):Oyun başlıyor")


def harita_ciz(satir, sutun):
    for i in range(satir):
        for j in range(sutun):
            if i == satir and j == sutun:
                print("X", end=" ")
            else:
                print("*", end=" ")
        print()


satir = 5
sutun = 8
sayac = 0
hazine_satir = random.randint(0, sutun)
hazine_sutun = random.randint(0, 3)
while hazine_satir == satir and hazine_sutun == sutun:
    hazine_satir = random.randint(0, sutun)
    hazine_sutun = random.randint(0, (satir + sutun + 1))
print("\nHarita")
harita_ciz(satir, sutun)
while True:
    hareket = input(f"(Sistem):W/A/S/D ile hareket et q ile kapat\n{isim}:->").upper()
    if hareket == "W" and satir > 0:
        satir -= 1
        sayac += 1
    elif hareket == "S" and satir < sutun:
        satir += 1
        sayac += 1
    elif hareket == "A" and sutun > 0:
        sutun -= 1
        sayac += 1
    elif hareket == "D" and sutun < (satir + sutun + 1):
        sutun += 1
        sayac += 1
    elif hareket == "Q":
        print("(Sistem):Oyundan çıkılıyor...")
        time.sleep(1)
        print("(Sistem):Oyunun Kodları siliniyor...")
        time.sleep(1)
        print("(Sistem):Oyundan aşarıyla çıkıldı!")
        break
    else:
        print("\n(Sistem):Böyle bir hareket tuşu yok.")
        break
    print("\nHarita")
    harita_ciz(satir, sutun)
    if satir == hazine_satir and sutun == hazine_sutun:
        print(
            "\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇"
        )
        print("(Sistem):Tebrikler! Oyunu kazandınız🎉🎉")
        print("(Sistem):Oyun kapatılıyor...")
        break
