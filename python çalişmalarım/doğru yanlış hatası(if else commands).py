deneme = input("deneme sadece harf calıscak")
if not deneme.isalpha():
    print("sadece harf")
    exit()
else:
    print("harf yazıldı")
#ÖNEMLİ!! #### isalpha yada isdigitin sonuna(): yazılmazsa sadece else çalışır.
#yukarıdaki else ise if not olduğu için doğru olan yani harf yazılırsa else çalışır ve print çalışır if çalısırsa exit() komudu çalısır ve komut durur
#yukarıdaki if not = isalpha eğer harf varsa onu kontrol eder not yazarsak if başka bir sayı yazıldığı sürece print komudundaki şeyi yazacak
denemo = input("sadece sayı çalıscak")
if not denemo.isdigit():
    print("sadece sayı")
    exit()
else:
    print("sayı yazıldı")
#yukarıdaki if not denemö.isdigit = sayımı değilmi diye kontrol eder ve sayı ise else çalışır harf ise if çalışır