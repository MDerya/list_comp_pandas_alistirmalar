
##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()


df.columns = ["NUM_"+i.upper() if df[i].dtype != "O" else i.upper() for i in df.columns]


# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns

df.columns = [i.upper()+"_FLAG" if "no" not in str(df[i]) else i.upper() for i in df.columns]

#ya da
df.columns = [i.upper() if "no" in i else i.upper()+"_FLAG" for i in df.columns]

# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns


new_cols= [df.drop(columns=["abbrev","no_previous"]) for i in df.columns] #drop kalıcı oldugu icin kullanırken dikkat et

new_cols

#ya da

og_list = ["abbrev", "no_previous"]
new_list=[i for i in df.columns if i not in og_list ]
print(df[new_list].head())


##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
df=sns.load_dataset("titanic")

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df["sex"].value_counts()


#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
#(unique : birbirinden farklı kaç kategori olduğunun bilgisi.)
df.nunique()
#df.nunique(axis=1) dersek her bir satıra ait unique degerlerin sayısı
#unique    degerleri/ nunique sayısını verir

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df["pclass"].unique()


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

df[["pclass","parch"]].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df["embarked"].dtypes  #embarked  liman bilgisi

df["embarked"] = df["embarked"].astype('category')
# tipini degistirmemizin sebebi
# kategorilere ayırmadan 7.görevi yapamayız,C olanları Q olanları rahatlıkla cekebiliriz
# object ile kategori arasındaki fark kategori de neye göre işlem yapabilecegimizi görmemiz


#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"]=="C"].head()


# df["embarked"]=="C"   buradan true false lu geliyor

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"]!="S"].head()

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df.loc[(df["age"] < 30) & (df["sex"]=="female")].head()

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df.loc[(df["fare"] > 500) | (df["age"] > 70)].head()


#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum()


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df.drop(["who"],axis=1).head()
#df.drop("who",axis=1)  bu da olur
#ya da

df.drop(columns=["who"]).head()

#ya da

df.columns.drop("who")

#########################################
# Görev 13: deck değiskenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################
#df["deck"].mode() bu kodu calıstırdıgımızda C yi 0.indexte gösteriyor,
# bu yüzden alttaki kodda mode un yanında [0] olarak belirttik
df["deck"]= df["deck"].fillna(df["deck"].mode()[0])

df["deck"].head()
#ya da

df["deck"].mode()
df["deck"].fillna(value="C", inplace=True) #burada modu al demedik,direk C yi al dedik

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df["age"]= df["age"].fillna(df["age"].median())

df["age"].head()

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında
# sum, count, mean değerlerini bulunuz.
#########################################
#sum ilgilendigimiz degerin toplamı,count kişi sayısı
df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})

#ya da
df.groupby(["pclass","sex"])["survived"].agg(["sum","count","mean"])

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

df["age_flag"] = df["age"].apply(lambda i: 1 if i<30 else 0)

df.head()

#ya da
def changer(age):
 if age < 30:
  return 1
 else:
  return 0

df["age_flag"] =df["age"].apply(lambda age: changer(age))

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

import seaborn as sns
df = sns.load_dataset("Tips")
df.head()

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})

#ya da

df.loc[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day")["total_bill", "tip"].agg(["sum", "min", "max", "mean"])


df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"],
                                                                            "lunch" : lambda x:  x.nunqiue() })

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

df.loc[(df["size"]<3) & (df["total_bill"]>10)].mean()

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

df["total_bill_tip_sum"]= df["total_bill"] + df["tip"]

df.head()
#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

df["total_bill_tip_sum"].sort_values()  #kücükten büyüge sıralar

df["total_bill_tip_sum"].sort_values(ascending=False)  #büyükten kücüge sıralar

df["new_total"]=df["total_bill_tip_sum"].sort_values(ascending=False).head(30)

df["new_total"]
df

#ya da
df["total_bill_tip_sum"].sort_values(ascending=False)[:30].reset_index(drop=True)
#ya da
new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape

############################################################################

def square(num): return num**2

numbers=[1,3,5,9]

print(list(map(square,numbers)))
#ya da
for i in map(square,numbers):
    print(i)