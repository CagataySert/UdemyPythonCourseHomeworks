"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.


"""

def frekans(kelime):
    kelime = list(kelime)

    kelime_sözlük = dict()

    for i in kelime:
        if (i in kelime_sözlük):
            kelime_sözlük[i] +=1
        else:
            kelime_sözlük[i] = 1

    for harf,sayı in kelime_sözlük.items():
        print("{} harfi {} defa geçmiştir...".format(harf,sayı))

x = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

frekans(x)

