######################
# Python Alıştırmalar
#######################

# Görev: 1
# Type inceleme

x = 8

y = 3.2

z = 8j + 18

a = "Hello World"

b = True

c = 23 < 22

l = [1, 2, 3, 4]

d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}

t = ("Machine Learning", "Data Science")

s = {"Python", "Machine Learning", "Data Science"}

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)

# Görev 2:
# Verilen string ifadenin tüm harflerini büyük harfe çevirme, virgülve nokta
yerine space koyunuz kelime kelime ayırınız

text = "The goal is to turn data info information, and information into insight"

text.replace("information,", "information").replace("insight.", "insight").upper().split()


# Görev 3:

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Listenin eleman sayısı

len(lst)

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağıralım

lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] oluşturmak

lst[0:4]

# Adım 4: Sekizinci indexteki elemanı sil

lst.pop(8)

# Adım 5: Yeni bir eleman ekleyiniz

lst.append("N")

# Adım 6: 8. indexe "N" elemanını yeniden ekleyiniz

lst.insert(8, "N")

# Görev 4:

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# Adım 1: Tüm Key değerlerine erişme

dict.keys()

# Adım 2: Valuelere erişme

dict.values()

# Adım 3: Daisy keyine ait 12 değerini 13 olarak güncelleme

dict["Daisy"] = ["England" ,"13"]

# Adım 4: Key değeri Ahmet value değeri [Turkey, 24] olan yeni bir değer ekleme

dict.update({"Ahmet": ["Turkey", 22]})

# Adım 5: Antonio'yu dictionary'den siliniz

dict.pop("Antonio")

# Görev 5: Argüman olarak bir liste olan, listenin içerisindeki tek ve çift
# ve bu sayıları ayrı listelere atayan ve bu listeleri return eden fonk yazın

l = [2, 13, 18, 93, 22]

def liste(l):
    A = []
    B = []
    for i in l:
        if i % 2 == 0:
         A.append(i)
        else:
         B.append(i)
    return A, B

A, B = liste(l)

print(A)
print(B)

#################################################################
# Görev 6: öğrenciler listesinde ilk 3 sıra müh den dereceye girenleri
# son 3 sıra tıp fak dereceye girenleri temsil etmeekte
# enumerate kullanarak öğrenci derecelerini fakülte özelinde yazdıralım

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

tip = ogrenciler[3:6]
muh = ogrenciler[0:3]

def students(fakulte, title):
    print(title)
    for index, element in enumerate(fakulte, 1):
        print(index, element)

    students(ogrenciler[3:6], "tip")
    student(ogrenciler[0:3], "muh")
##################################################
# Görev 7:
# sırası ile dersin kodu, kredisi, kontenjan bilgisi
# zip ile ders bilgisini bastıracağız

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

list(zip(ders_kodu, kredi, kontenjan))

# Görev 8: Aşağıda 2 adet set verilmiştir
# 1. küme 2. kümeyi kapsıyor ise ortak elemanlarını
# eğer kapsamıyorsa 2. kümenin birinci kümeden farkını

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def fark_set(kume1, kume2):
        if kume1.issuperset(kume2):
            print(kume1.intersection(kume2))
        else:
            print(kume2.difference(kume1))

fark_set(kume1, kume2)

