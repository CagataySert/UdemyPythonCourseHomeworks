"""
Problem 3
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.
"""
def dogrulama(liste):
    son_liste = list()
    for i in liste:
        if i.endswith("@gmail.com") or i.endswith("@hotmail.com") or i.endswith("@yahoo.com"):
            son_liste.append(i)
        else:
            continue
    return print(son_liste)

with open("mailler.txt","r",encoding="utf-8") as file:
    mail_icerigi = file.read()
    mailler = mail_icerigi.split()
    dogrulama(mailler)