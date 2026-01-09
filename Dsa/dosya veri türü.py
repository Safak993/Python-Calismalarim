#file(dosya) veri türü
import os
# dosya açarken:
#     w: yazma (write)
#     r: okuma(read)
#     a: Ekleme(append)
#Dosyaya yazma
# dosya = open("merhaba.txt","w") # yazma modunda dosya açma
# satir = "Hello world\nMerhaba dünya\n"
# dosya.write(satir)# dosyaya metin yazdırılması
# dosya.close()

# Dosyadan okuma

dosya = open("merhaba.txt", "r") # okuma modunda

#karakter okuma:
#metin = dosya.read(12)#12 karakter oku
#print(metin)
#dosya.close()

#dosyadan satır okuma:
satir = dosya.readlines()
print(satir)
dosya.close()
os.remove("merhaba.txt")