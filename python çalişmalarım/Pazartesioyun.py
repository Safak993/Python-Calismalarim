print("Albion'da en sevdiginiz silah hangisidir?")

favori_silah = input('Favori silahim: ') #başarılı şekilde değişkene veri aldık

# print(favori_silah) # bunu aldığımızı teyit ettik, harbiden almışız

print("Demek favori silahın "+ favori_silah + " he. Vay be. Sence güçlü mü?") #favori silah daima isim olacağından hep str geleceğini tahmin ettik

guclu_mu = input("Bence silahim (guclu/orta/zayif) ")

# print(guclu_mu) #başarılı #başarılı olanların testini yaptığımız satırları ctrl ö ile yorum satırı yaparak silmekle uğraşmadan devam ederiz, en son lazım olursa tekrar açarız ya da gerkemezse takır takır sileriz


if (guclu_mu == "guclu"):
    # güçlü cevabı geldiyse
    print("Diyorsun ki " + favori_silah + " " + guclu_mu + ". Bence o kadar guclu olamaz. ")
elif (guclu_mu == "orta"):
    # orta cevabı geldiyse
    print("Diyorsun ki " + favori_silah + " " + guclu_mu + ". Bence de orta seviye bir silah. ")
elif (guclu_mu == "zayif"):
    # zayif cevabi geldiyse
    print("Diyorsun ki " + favori_silah + " " + guclu_mu + ". Abartma, uygun buildle fena bişi oluyor o. ")
else: #cevaplardan biri gelmediyse
    print("Sen de oynadığın silahi tarif edemiyorsun hee. Ne dedin anlayamadım")
