#Rastgele sayı oyunu!!
import random
isim = (input("\n(sistem):Oyun için ismini gir\n(kullanıcı):->"))#isim yazdırma 
sayi = random.randint(1,100)#random sayı
count = 0#tekrarlama(döngü)
while True:
    tahmin = int(input(f"\n(sistem): 1 ile 100 arasında bir sayı tut\n({isim}):->"))#Rastgele sayıyı tahmin etme
    count += 1
    if tahmin == sayi:
       print(f"Doğru bildin ({isim})\n{count} denemede buldun.")#doğru bilince seçtiğin isim yazması ve kaç denemede yaptığın
       break
    else:
        print(f"seçtiğin sayı yanlıştı({isim})")#yanlış cevap
        print("Tekrar dene")
