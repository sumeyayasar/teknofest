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

sns.scatterplot(x="studytime", y="G3", data=df)
sns.regplot(x="studytime", y="G3", data=df)
plt.title("studytime vs Final grade")
plt.xlabel("studytime")
plt.ylabel("G3")
plt.grid(alpha=0.3)
plt.show()

print("1)Scatter plot incelendiğinde çalışma süresi ile final notu arasında pozitif yönlü ncak zayıf bir ilişki gözlemlenmektedir.Regrasyon dorğrusu yukarı eğimli olsa da veri noktalarının geniş bir alana yayılması ilişkinin güçlü olmadığını göstermektedir.Ayrıca bazı öğrencilerin çalışma süresi yüksek olmasına rağmen düşük not aldığı gözlemlenmiştir;bu durum aykırı değerlerin veya ek değişkenlerin etkisini düşündürmektedir.")

#Devamsızlık ile final notu arasında negatif bir ilişki var mı?
df["abs_bin"] = pd.cut(
    df["absences"],
    bins=[0,5,10,15,20],
    labels=["0-5","6-10","11-15","16-20"]
)
plt.figure(figsize=(8,5))

sns.boxplot(
    x="abs_bin",
    y="G3",
    data=df
)
plt.title("Devamsızlık ile Final Notu İlişkisi")
plt.xlabel("Devamsızlık Gün Aralığı")
plt.ylabel("Final Notu (G3)")

plt.show()
print("Boxplot grafiği incelendiğinde devamsızlık gün sayısı arttıkça final notlarının genel olarak düşme eğiliminde olduğu görülmektedir. Bununla birlikte not dağılımlarının gruplar arasında büyük ölçüde örtüşmesi, devamsızlık ile final notu arasında güçlü bir ilişki bulunmadığını, ancak zayıf bir negatif ilişki olabileceğini göstermektedir.")
#G1 ve G2 notları G3 notunu ne kadar iyi tahmin ediyor?
plt.figure(figsize=(10,4))

#  G1 - G3
plt.subplot(1,2,1)

corr_g1 = df[["G1","G3"]].corr()

sns.heatmap(
    corr_g1,
    annot=True,
    cmap="coolwarm",
    vmin=-1, vmax=1,
    square=True
)
plt.title("G1 ve G3 Korelasyonu")

# G2 - G3
plt.subplot(1,2,2)

corr_g2 = df[["G2","G3"]].corr()

sns.heatmap(
    corr_g2,
    annot=True,
    cmap="coolwarm",
    vmin=-1, vmax=1,
    square=True
)
plt.title("G2 ve G3 Korelasyonu")
plt.tight_layout()
plt.show()
print("korelasyon analizine göre G1 ve G2 notları ile G3 arasında giçli pozitif ilişkiler bulunmaktadır.özellikle G2 notunun G3 ile olan korelasyonu daha yüksek olup,öğrenciler ikinci dönem performanslarının final başarısını daha güçlü şekilde yansıttığı görülmektedir.")

# Daha önce sınıf tekrar eden öğrenciler (failures) daha düşük not mu alıyor?
df["failures"] = df["failures"].astype(int)
plt.figure(figsize=(8,5))

sns.boxplot(
    x="failures",
    y="G3",
    data=df
)
plt.title("Sınıf Tekrarı ile Final Notu İlişkisi")
plt.xlabel("Sınıf Tekrarı Sayısı")
plt.ylabel("Final Notu (G3)")
plt.show()
print("Sınıf tekrarı sayısına göre oluşturulan boxplot grafiği incelendiğinde, sınıf tekrarı yapmayan öğrencilerin final notlarının daha yüksek ve daha dengeli bir dağılım gösterdiği görülmektedir. Sınıf tekrarı sayısı arttıkça medyan final notunun kademeli olarak düştüğü ve not dağılımının daha geniş hale geldiği gözlemlenmiştir. Özellikle birden fazla sınıf tekrarı yapan öğrencilerde düşük notların daha yaygın olduğu dikkat çekmektedir. Bu bulgular, sınıf tekrarı ile akademik başarı arasında negatif yönlü bir ilişki olabileceğini göstermektedir. Ancak ilişkinin nedensel bir sonuç ifade etmediği ve öğrencilerin başarısını etkileyen farklı faktörlerin de bulunabileceği göz önünde bulundurulmalıdır.")

#Ekstra özel ders (paid) alan öğrencilerin notları daha yüksek mi?
plt.figure(figsize=(6,5))

sns.boxplot( x="paid",y="G3",data=df)

plt.title("Ekstra Özel Ders (Paid) ile Final Notu İlişkisi")
plt.xlabel("Ekstra Özel Ders Alıyor mu?")
plt.ylabel("Final Notu (G3)")

plt.grid(alpha=0.3)
plt.show()
print("Boxplot grafiği incelendiğinde, ekstra özel ders alan ve almayan öğrencilerin medyan final notları yaklaşık 11 olarak gözlemlenmektedir. Özel ders alan grupta bazı aykırı değerler bulunmakta, bu durum bazı öğrencilerin performansının grup ortalamasından farklı olabileceğini göstermektedir")

# ******************************
#        AİLE FAKTÖRLERİ
# ******************************

#Anne eğitim seviyesi (Medu) arttıkça öğrencinin başarısı artıyor mu?
plt.figure(figsize=(8,5))
sns.boxplot(x="Medu", y="G3", data=df)

plt.title("Anne Eğitim Seviyesi ile Final Notu İlişkisi")
plt.xlabel("Anne Eğitim Seviyesi (0-4)")
plt.ylabel("Final Notu (G3)")
plt.grid(alpha=0.3)
plt.show()
print("Anne eğitim seviyesi arttıkça öğrencilerin final notlarında genel bir yükseliş gözlemlenmektedir. Özellikle yüksek eğitim seviyesine sahip annelerin çocuklarında medyan notlar daha yüksek olma eğilimindedir. Bununla birlikte, bazı öğrenciler bu grupta beklenenden düşük notlar almış, yani aykırı değerler mevcuttur; bu durum, yüksek anne eğitim seviyesine rağmen bazı öğrencilerin düşük performans gösterebileceğini ortaya koymaktadır. Genel olarak, anne eğitim seviyesi ile öğrencinin başarısı arasında pozitif bir ilişki olduğu söylenebilir, ancak tek başına başarıyı garanti etmemektedir")

#Baba eğitim seviyesi (Fedu) öğrencinin notlarını etkiliyor mu?
plt.figure(figsize=(8,5))
sns.boxplot(x="Fedu", y="G3", data=df)

plt.title("baba Eğitim Seviyesi ile Final Notu İlişkisi")
plt.xlabel("baba Eğitim Seviyesi (0-4)")
plt.ylabel("Final Notu (G3)")
plt.grid(alpha=0.3)
plt.show()

print("7)Baba eğitim seviyesi ile final notları arasında net bir ilişki yoktur.")

#Aile ilişkileri kalitesi (famrel) yüksek olan öğrenciler daha başarılı mı?

plt.figure(figsize=(8,5))

sns.boxplot(x="famrel", y="G3",data=df)

plt.title("Aile İlişkileri Kalitesi ile Final Notu İlişkisi")
plt.xlabel("Aile İlişkileri Kalitesi (1-5)")
plt.ylabel("Final Notu (G3)")
plt.grid(alpha=0.3)
plt.show()

print("8)Grafik incelendiğinde, aile ilişkileri puanı yüksek olan öğrencilerin genel olarak daha yüksek final notları aldığı gözlemlenmektedir. Ancak bazı öğrenciler düşük aile ilişkisi puanına sahip olmalarına rağmen yüksek not alabilmektedir. Bu nedenle, aile ilişkileri ile akademik başarı arasında hafif pozitif bir ilişki vardır.")

#Aile desteği (famsup) alan öğrencilerin notları daha iyi mi?
plt.figure(figsize=(6,5))

sns.boxplot(x="famsup",y="G3",data=df)

plt.title("Aile Desteği (famsup) ile Final Notu İlişkisi")
plt.xlabel("Aile Desteği Alıyor mu?")
plt.ylabel("Final Notu (G3)")
plt.grid(alpha=0.3)
plt.show()
print("9)Aile desteği (famsup) öğrencilerin final notları üzerinde belirgin bir etki göstermemektedir; bazı öğrenciler destek almamalarına rağmen yüksek başarı göstermektedir.")

#Anne ve babası birlikte yaşayan öğrenciler (Pstatus) daha başarılı mı?
plt.figure(figsize=(6,5))

sns.boxplot(x="Pstatus",y="G3",data=df)

plt.title("Ailenin Birlikte Yaşaması ile Final Notu İlişkisi")
plt.xlabel("Ailesi Birlikte mi Yaşıyor?")
plt.ylabel("Final Notu (G3)")
plt.grid(alpha=0.3)
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
sns.boxplot(x="activities", y="ortalama_not", data=df)
plt.title("Activities vs ortalama not")
plt.show()

print("12)Okul aktivitelerine katılım, öğrencilerin başarısında hafif bir artış eğilimi göstermektedir; ancak fark çok belirgin değildir.")

#Evde interneti olan öğrenciler (internet) daha yüksek not alıyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.boxplot(x="internet", y="ortalama_not", data=df)
plt.title("internet vs ortalama not")
plt.show()

internet_table = df.groupby("internet")[["G1","G2","G3","ortalama_not"]].mean().reset_index()
print(internet_table)

print("13)Evde internet erişimi, öğrencilerin genel başarıları üzerinde hafif olumlu bir etkiye sahiptir.")

# Kreşe gitmiş olmak (nursery) akademik başarıyı etkiliyor mu?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.boxplot(x="nursery", y="ortalama_not", data=df)
plt.title("nursery vs ortalama not")
plt.show()
nursery_table = df.groupby("nursery")[["G1","G2","G3","ortalama_not"]].mean().reset_index()
print(nursery_table)
print("14)Kreşe gitmiş olmak, öğrencilerin genel başarıları üzerinde hafif olumlu bir etkiye sahiptir.")

# ******************************************
#              SOSYAL HAYAT
# *****************************************

#Arkadaşlarla dışarı çıkma sıklığı (goout) arttıkça notlar düşüyor mu?
plt.figure(figsize=(8,5))

sns.boxplot(x="goout",y="G3",data=df)

plt.title("Haftalık Dışarı Çıkma Sıklığı ile Final Notu İlişkisi")
plt.xlabel("Haftada Kaç Gün Dışarı Çıkıyor?")
plt.ylabel("Final Notu (G3)")
plt.grid(alpha=0.3)
plt.show()
print("15)Arkadaşlarla sık dışarı çıkmak, öğrencilerin genel başarılarını düşürme eğilimindedir.")

#Romantik ilişkisi olan öğrencilerin (romantic) akademik performansı farklı mı?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.boxplot(x="romantic", y="ortalama_not", data=df)
plt.title("romantic vs ortalama not")
plt.show()
print("16)Romantik ilişki,öğrencilerin genel başarıları üzerinde hafif olumsuz bir etkiye sahiptir.")

# Boş zaman miktarı (freetime) fazla olan öğrencilerin notları daha mı düşük?
df["ortalama_not"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.boxplot(x="freetime", y="ortalama_not", data=df)
plt.title("freetime vs ortalama not")
plt.show()
freetime_table = df.groupby("freetime")[["G1","G2","G3","ortalama_not"]].mean().reset_index()
print(freetime_table)
print("17)Boş zaman miktarı ile akademik başarı arasında net bir ilişki gözlemlenmemektedir; dağılım düzensizdir.")

#*********************************
#          YAŞAM TARZI
#*********************************

#Hafta içi alkol tüketimi (Dalc) akademik başarıyı etkiliyor mu?
df["Avg"] = (df["G1"] + df["G2"] + df["G3"]) / 3
df['Dalc_yesno']=df['Dalc'].apply(lambda x:"yes" if x>1 else"no")
plt.figure(figsize=(6,5))
sns.boxplot(x="Dalc_yesno", y="Avg", data=df)

plt.title("Hafta İçi Alkol Tüketimi ile Akademik Başarı İlişkisi")
plt.xlabel("Hafta İçi Alkol Tüketimi (1-5)")
plt.ylabel("Ortalama Not")
plt.grid(alpha=0.3)
plt.show()
print("18)Hafta içi alkol kullanmayan öğrencilerin notları biraz daha yüksek olsa da fark çok belirgin değildir.")

#Hafta sonu alkol tüketimi (Walc) notları düşürüyor mu?
df["Avg"] = (df["G1"] + df["G2"] + df["G3"]) / 3
df['Walc_yesno']=df['Walc'].apply(lambda x:"yes" if x>1 else"no")
plt.figure(figsize=(6,5))
sns.boxplot( x="Walc_yesno",y="Avg",data=df)

plt.title("Hafta Sonu Alkol Tüketimi ile Akademik Başarı")
plt.xlabel("Hafta Sonu Alkol Tüketimi (No=1, Yes>1)")
plt.ylabel("Ortalama Not")
plt.show()
print("19)Hafta sonu alkol tüketimi öğrencilerin notlarını etkilememektedir.")

#Sağlık durumu (health) ile akademik başarı arasında ilişki var mı?
df["Avg"] = (df["G1"] + df["G2"] + df["G3"]) / 3
sns.boxplot(x="health", y="Avg", data=df)
plt.title("health vs ortalama not")
plt.show()
print("20)Daha iyi sağlık durumu olan öğrencilerin ortalama notları biraz daha yüksek olsa da fark çok belirgin değildir.")










