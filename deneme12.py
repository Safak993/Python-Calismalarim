import os
with open ("SA123.txt", "a") as E:
    (E.write("sa"))
with open ("SA123.txt", "r") as E:
    print(E.read)
os.remove("SA123.txt")