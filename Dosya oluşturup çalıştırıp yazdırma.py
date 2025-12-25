import os
with open("deneme1.py", "a") as E:
    E.write("def main(a, b):")
    E.write("\n    a = 5 # kodlar")
    E.write("\n    b = 10 # kodlar")
    E.write("\n    print(a + b) #kodlar")
    E.write("\nprint('Cevap')")
assagi = "↓"
a = 1
b = 1
with open("deneme1.py", "r") as E:
    kod = E.read()
    print(kod)
import deneme1
deneme1.main(a, b)
os.remove("deneme1.py")
