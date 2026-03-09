import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#veriyi yükleme
df = pd.read_csv("student_data.csv")

# ******************************************
#        AKADEMİK BAŞARI İLE İLGİLİ
# ******************************************


#çalışma süresi arttıkça final notu artuyor mu?

sns.lineplot(x="studytime", y="G3", data=df)
plt.title("studytime vs Final grade")
plt.show()
plt.xlabel("studytime")
plt.ylabel("G3")

print("1)studytime ile final g arasında zayıf bir pozitif ilişki gözlemlenmiştir.")

#Devamsızlık ile final notu arasında negatif bir ilişki var mı?
sns.lineplot(x="absences", y="G3", data=df)
plt.title("absences vs Final grade")
plt.show()
plt.xlabel("absences")
plt.ylabel("G3")

print("2)devamsızlık ile final notu arasında zayıf negatif bir ilişki gözlemlenmiştir.Ancak bu tek başına final notunu güçlü bir şekilde belirlemez.")

#ilk dönem notu(G1) ve ikinci dönem notu(G2) ,final notunu (G3) ne kadar iyi tahmin eder?
sns.lineplot(x="G1", y="G3", data=df)
plt.title("G1 vs Final Grade")
plt.show()

sns.lineplot(x="G2", y="G3", data=df)
plt.title("G2 vs Final Grade")
plt.show()

print("3)G1 ve G2 notları ile final notu arasında güçlü pozitif bir ilişki bulunmaktadır. Notlar arttıkça final notunun da arttığı görülmektedir.")

# Daha önce sınıf tekrar eden öğrenciler (failures) daha düşük not mu alıyor?
sns.lineplot(x="failures",y="G3",data=df)
plt.xlabel("failures")
plt.ylabel("G3")
plt.title("failures-G3 Graph")
plt.show()
print("4)Sınıf tekrar eden öğrencilerin  notlarının daha düşük olduğu görülmüştür.")

#Ekstra özel ders (paid) alan öğrencilerin notları daha yüksek mi?
plt.subplot(1,2,1)
sns.barplot(x="paid", y="G3", data=df)
plt.title("paid-G3 Graph")
plt.show()

print("5)Özel ders alan öğrenciler biraz daha yüksek not alma eğilimindedir, fakat fark belirgin değildir.")

# ******************************
#        AİLE FAKTÖRLERİ
# ******************************

#Anne eğitim seviyesi (Medu) arttıkça öğrencinin başarısı artıyor mu?
plt.subplot(1,2,1)
sns.barplot(x="Medu", y="G3", data=df)
plt.title("Medu-G3 Graph")
plt.show()

print("6)Grafiğe göre, annesi eğitim almamış öğrenciler (Medu = 0) en yüksek final notlarını alırken, eğitim seviyesi arttıkça notlar düzenli bir şekilde yükselmiyor. Örneğin Medu = 4 olan öğrencilerin notları, Medu = 0 grubunun altında kalıyor. Bu durum,anne eğitim seviyesi ile öğrencinin final başarısı arasında belirgin ve düzenli bir pozitif ilişki olmadığını göstermektedir.")

#Baba eğitim seviyesi (Fedu) öğrencinin notlarını etkiliyor mu?

plt.subplot(1,2,1)
sns.barplot(x="Fedu", y="G3", data=df)
plt.title("Fedu-G3 Graph")
plt.show()

print("7)Baba eğitim seviyesi ile final notları arasında net bir ilişki yoktur.")

#Aile ilişkileri kalitesi (famrel) yüksek olan öğrenciler daha başarılı mı?

sns.barplot(x="famrel", y="G3", data=df)
plt.title("Family Relationship vs Final Grade")
plt.xlabel("famrel")
plt.ylabel("G3")
plt.show()

print("8)Grafik incelendiğinde, aile ilişkileri puanı yüksek olan öğrencilerin genel olarak daha yüksek final notları aldığı gözlemlenmektedir. Ancak bazı öğrenciler düşük aile ilişkisi puanına sahip olmalarına rağmen yüksek not alabilmektedir. Bu nedenle, aile ilişkileri ile akademik başarı arasında hafif pozitif bir ilişki vardır.")

#Aile desteği (famsup) alan öğrencilerin notları daha iyi mi?

sns.barplot(x="famsup", y="G3", data=df)
plt.title("Famsup vs Final Grade")
plt.xlabel("famsup")
plt.ylabel("G3")
plt.show()

print("9)Aile desteği (famsup) öğrencilerin final notları üzerinde belirgin bir etki göstermemektedir; bazı öğrenciler destek almamalarına rağmen yüksek başarı göstermektedir.")

#Anne ve babası birlikte yaşayan öğrenciler (Pstatus) daha başarılı mı?
sns.barplot(x="Pstatus", y="G3", data=df)
plt.title("Pstatus vs Final Grade")
plt.xlabel("Pstatus")
plt.ylabel("G3")
plt.show()

print("10)Ebeveynlerin birlikte veya ayrı yaşaması, öğrencilerin akademik başarısını belirlemede tek başına belirleyici bir faktör değildir. Ayrı yaşayan öğrenciler de yüksek başarı gösterebilir.")


# ******************************************
#        OKUL VE ÇEVRESEL FAKTÖRLER
# ******************************************

# Okula ulaşım süresi (traveltime) uzun olan öğrencilerin notları daha düşük mü?
sns.lineplot(x="traveltime",y="G3",data=df)
plt.xlabel("traveltime")
plt.ylabel("G3")
plt.title("traveltime-G3 Graph")
plt.show()

print("11)ulaşım süresi uzun olan öğrencilerin notları daha düşüktür")

#Okul aktivitelerine katılan öğrenciler (activities) daha başarılı mı?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="activities", y="ortalama_not", data=df)
plt.title("Activities vs ortalama not")
plt.show()

print("12)Okul aktivitelerine katılım, öğrencilerin başarısında hafif bir artış eğilimi göstermektedir; ancak fark çok belirgin değildir.")

#Evde interneti olan öğrenciler (internet) daha yüksek not alıyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="internet", y="ortalama_not", data=df)
plt.title("internet vs ortalama not")
plt.show()

internet_table = df.groupby("internet")[["G1","G2","G3","ortalama_not"]].mean().reset_index()
print(internet_table)

print("13)Evde internet erişimi, öğrencilerin genel başarıları üzerinde hafif olumlu bir etkiye sahiptir.")

# Kreşe gitmiş olmak (nursery) akademik başarıyı etkiliyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="nursery", y="ortalama_not", data=df)
plt.title("nursery vs ortalama not")
plt.show()
nursery_table = df.groupby("nursery")[["G1","G2","G3","ortalama_not"]].mean().reset_index()
print(nursery_table)
print("14)Kreşe gitmiş olmak, öğrencilerin genel başarıları üzerinde hafif olumlu bir etkiye sahiptir.")

# ******************************************
#              SOSYAL HAYAT
# *****************************************

#Arkadaşlarla dışarı çıkma sıklığı (goout) arttıkça notlar düşüyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.lineplot(x="goout", y="ortalama_not", data=df)
plt.title("Going Out vs Ortalama not")
plt.show()
print("15)Arkadaşlarla sık dışarı çıkmak, öğrencilerin genel başarılarını düşürme eğilimindedir.")

#Romantik ilişkisi olan öğrencilerin (romantic) akademik performansı farklı mı?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="romantic", y="ortalama_not", data=df)
plt.title("romantic vs ortalama not")
plt.show()
print("16)Romantik ilişki,öğrencilerin genel başarıları üzerinde hafif olumsuz bir etkiye sahiptir.")

# Boş zaman miktarı (freetime) fazla olan öğrencilerin notları daha mı düşük?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="freetime", y="ortalama_not", data=df)
plt.title("freetime vs ortalama not")
plt.show()
freetime_table = df.groupby("freetime")[["G1","G2","G3","ortalama_not"]].mean().reset_index()
print(freetime_table)
print("17)Boş zaman miktarı ile akademik başarı arasında net bir ilişki gözlemlenmemektedir; dağılım düzensizdir.")

#*********************************
#          YAŞAM TARZI
#*********************************

#Hafta içi alkol tüketimi (Dalc) akademik başarıyı etkiliyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="Dalc", y="ortalama_not", data=df)
plt.title("Dalc vs ortalama not")
plt.show()
print("18)Hafta içi alkol kullanmayan öğrencilerin notları biraz daha yüksek olsa da fark çok belirgin değildir.")

#Hafta sonu alkol tüketimi (Walc) notları düşürüyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="Walc", y="ortalama_not", data=df)
plt.title("Walc vs ortalama not")
plt.show()
print("19)Hafta sonu alkol tüketimi öğrencilerin notlarını etkilememektedir.")

#Sağlık durumu (health) ile akademik başarı arasında ilişki var mı?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.barplot(x="health", y="ortalama_not", data=df)
plt.title("health vs ortalama not")
plt.show()
print("20)Daha iyi sağlık durumu olan öğrencilerin ortalama notları biraz daha yüksek olsa da fark çok belirgin değildir.")










