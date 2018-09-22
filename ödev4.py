"""
Problem 4
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek ,
ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""
def tuple(i):
    return i[0]




isim = ["Kerim","Tarık","Ezgi","Kemal","Ilkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isim,soyisim))
print(liste)
liste.sort(key=tuple)

print(liste)
"""liste = list(zip(isim,soyisim))

print(list(sorted(liste,key=tuple)))"""

