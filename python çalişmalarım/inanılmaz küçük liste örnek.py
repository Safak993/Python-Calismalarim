#----Küçük liste örnekleri----#
#----Listeler----#
konusma = ["OYUN OYNUYOM", "OYUNDAYIM", "OYUN OYNUYORUM"] #listeleme
konusma_2 = ["NASILSIN", "NABER", "İYİMİSİN"]
#----Döngüleme----#
while True:
    konus = input("\nkonuş\n(kullanıcı):").upper() #büyük harfe çevirme
    # print(konus)
    # print(konusma[0])
    if konus in (tuple(konusma)): # konusma 1 in cevapları
        print("Güzel bende oyun severim")
    if konus in (tuple(konusma_2)): #konusma 2 nin cevapları
        print("İyi senden?")
