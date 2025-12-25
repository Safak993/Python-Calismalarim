#----Dosya oluşturup içine bişeyler yazdırıp silme----#
import os # os.removenin kullanımı
#----Ana kod----#

with open("deneme.txt", "a") as E: # E bir değişken gibidir q bile olsa çalışır
  E.write("\n(Sistem): Naber\n (Kullanıcı): İyi senden naber") # e dosyanın kendisidir e.write dosyanın kendisine bişiler yazdırma

with open("deneme.txt" "r") as E: # dosyayı açma # "r" ise dosyayı okuma
  print(E.read()) # dosyanın içindekini yazdırma

os.remove("deneme.txt") # dosyayı silme