#| Tür      | Ne demek   | Örnek          |
#| -------- | ---------- | -------------- |
#| O(1)     | Anında     | İlk elemanı al |
#| O(n)     | Tek tek    | Listeyi dolaş  |
#| O(log n) | Yarıya böl | Sayı tahmini   |
#| O(n²)    | Çok yavaş  | Herkese herkes |
#####################################################
# | KELİME     | NE?                 | EN BASİT ANLAM      |
# |------------|---------------------|---------------------|
# | class      | Kalıp               | Şablon              |
# | obje       | Class’tan çıkan     | Gerçek şey          |
# | __init__   | Başlangıç fonksiyonu| Doğunca çalışır     |
# | self       | Kime ait            | Ben                 |
# | self.x     | Özellik             | Bana ait bilgi      |
# | def f(self)| Davranış            | Ne yapabiliyor      |
#############################################################
# | KOD PARÇASI              | NE OLUYOR?                    |
# |--------------------------|-------------------------------|
# | class Ogrenci:           | Öğrenci kalıbı                |
# | __init__ çalışır         | Öğrenci oluşturuldu           |
# | self.ad = ad             | Bu öğrencinin adı             |
# | self.yas = yas           | Bu öğrencinin yaşı            |
# | ogr = Ogrenci("Ali",12)  | Ali adlı öğrenci oluştu        |
# | ogr.ad                   | Ali                            |
################################################################
# | NEDEN self VAR? | CEVAP                      |
# |-----------------|----------------------------|
# | Birden fazla obje | Herkesin bilgisi ayrı    |
# | Bilgi saklamak    | Değer kaybolmaz           |
# | Karışıklık yok    | Kime ait belli            |
######################################################
# | self YOKSA | NE OLUR?              |
# |------------|-----------------------|
# | Bilgi ortak| Herkes aynı olur      |
# | Karışıklık | Kime ait belli değil  |
# | Oyun olmaz | Oyuncular kopya       |
class hayvan:
    def __init__(self, tavuk_sesi, inek_sesi,):
        self.tavuk = tavuk_sesi
        self.inek = inek_sesi
h = hayvan("bıg bıg bıdak","mööööö")
print(f"{h.tavuk}\n {h.inek}")
# ARRAY     | LİNKED LİST
#----------------------------------
#MEMORY LOCALİTY İÇİN İYİ|ELEMAN EKLEMEK SİLMEK
#           |ARRAYLARE GÖRE DAHA KOLAY
#           |
#           |
