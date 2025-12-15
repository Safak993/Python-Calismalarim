import random
isim = (input("\n(sistem):Oyun için ismini gir\n(kullanıcı):->"))
sayi = random.randint(1,100)
count = 0
while True:
    tahmin = int(input(f"\n(sistem): 1 ile 100 arasında bir sayı tut\n({isim}):->"))
    count += 1
    if tahmin == sayi:
       print(f"Doğru bildin ({isim})\n{count} denemede buldun.")
       break
    else:
        print(f"seçtiğin sayı yanlıştı({isim})")
        print("Tekrar dene")