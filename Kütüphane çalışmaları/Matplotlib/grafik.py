import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("personel_ist.csv")  # 👈 AYRAÇ DOĞRU

print(df.columns.tolist())  # ['ad', 'yas', 'maas']

# plt.plot(df['ad'], df['maas'])
# plt.plot(df['ad'], df['yas'])
# plt.xlabel("İsimler")
# plt.ylabel("Yaşlar")
# plt.title("Ad & Yaş grafiği")
# plt.subplot(1, 2, 2), plt.plot(df['ad'], df['yas'])
# plt.plot(df['ad'], df['maas'])

# plt.scatter(df['ad'], df['maas'])
# plt.scatter(df['ad'], df['yas'])
# plt.hist(df['maas'])#kaç kişide nekadar maaş var 2kişide şuadar maaş var falan fisıo
# plt.pie(df['maas'], labels = df['ad'])#külüstür şeklinde karşılaştırma en az olanın çubuk en küçük
plt.show()

# ----------------------------------------------------------------------------------------------------------------#
# ==============================
# MATPLOTLIB GRAFİKLER REHBERİ
# ==============================

# 1️⃣ Line Plot (Çizgi Grafiği)
# - Temel grafik, iki veri kümesi arasındaki ilişkiyi gösterir.
# - Kullanım: plt.plot(x, y)
# - Renk: 'r' = kırmızı, 'g' = yeşil, 'b' = mavi, '#FF5733' = hex kod
# - Stil: '-' = düz çizgi, '--' = kesikli, '-.' = noktalı-kesikli, ':' = noktalı
# Örnek: plt.plot(x, y, color='g', linestyle='--', marker='o')

# 2️⃣ Bar Chart (Çubuk Grafiği)
# - Kategorik veriler için ideal, x ekseni kategorik, y sayısal
# - Kullanım: plt.bar(x, y)
# - Renk: color='blue' veya color='#00FF00'
# - Yatay çubuk: plt.barh(x, y)
# Örnek: plt.bar(df['ad'], df['maas'], color='#FF5733')

# 3️⃣ Scatter Plot (Dağılım Grafiği)
# - Noktalar ile iki sayısal veri arasındaki ilişkiyi gösterir
# - Kullanım: plt.scatter(x, y)
# - Renk ve boyut: color='r', s=50 (boyut)
# Örnek: plt.scatter(df['yas'], df['maas'], color='purple', s=100)

# 4️⃣ Histogram (Frekans Grafiği)
# - Sayısal verilerin dağılımını gösterir
# - Kullanım: plt.hist(data, bins=10)
# - Renk: color='skyblue'
# - bins = bölünecek aralık sayısı
# Örnek: plt.hist(df['yas'], bins=5, color='orange', edgecolor='black')

# 5️⃣ Pie Chart (Pasta Grafiği)
# - Oranları göstermek için ideal
# - Kullanım: plt.pie(sizes, labels=etiketler, autopct='%1.1f%%')
# - Renk: colors=['red', 'green', 'blue']
# Örnek: plt.pie([30, 20, 50], labels=['A','B','C'], colors=['#FF0000','#00FF00','#0000FF'], autopct='%1.1f%%')

# 6️⃣ Stack Bar Chart (Yığılı Çubuk)
# - Birden fazla kategori yığını göstermek için
# - Kullanım: plt.bar(x, y1, label='y1'), plt.bar(x, y2, bottom=y1)
# - Renk: color='blue', color='red'

# 7️⃣ Area Plot (Alan Grafiği)
# - Line plot’un altını doldurur, değişimi vurgular
# - Kullanım: plt.fill_between(x, y, color='skyblue', alpha=0.5)

# 8️⃣ Step Plot (Basamak Grafiği)
# - Veriler basamaklı görünür
# - Kullanım: plt.step(x, y, color='r', where='mid')

# 9️⃣ Error Bar (Hata Çubuklu Line Plot)
# - Verideki hata payını göstermek için
# - Kullanım: plt.errorbar(x, y, yerr=hatalar, fmt='o', color='b')

# 10️⃣ Box Plot (Kutu Grafiği)
# - Veri dağılımının çeyreklerini gösterir
# - Kullanım: plt.boxplot(data)
# - Örnek: plt.boxplot(df['maas'], patch_artist=True, boxprops=dict(facecolor='skyblue'))

# 11️⃣ Stackplot (Yığılmış Alan Grafiği)
# - Birden fazla veri setini alt alta gösterir
# - Kullanım: plt.stackplot(x, y1, y2, y3, colors=['r','g','b'])

# 12️⃣ Hexbin Plot (Yoğunluk Grafiği)
# - Büyük veri setlerinde dağılım yoğunluğu
# - Kullanım: plt.hexbin(x, y, gridsize=30, cmap='Blues')

# 13️⃣ Quiver Plot (Oklar)
# - Vektör alanlarını göstermek için
# - Kullanım: plt.quiver(X, Y, U, V, color='r')

# 14️⃣ 3D Plot (3 Boyutlu Grafik)
# - from mpl_toolkits.mplot3d import Axes3D
# - ax = fig.add_subplot(111, projection='3d')
# - ax.plot(x, y, z) veya ax.scatter(x, y, z)
# - Renk: c='red', marker='o'
