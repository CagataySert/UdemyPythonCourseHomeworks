"""Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek
bir string oluşturun ve bu string'i ekrana yazdırın."""

with open("şiir.txt","r",encoding="utf-8") as file:
    dosya_icerigi = file.read()
    liste = list()
    kelimeler = dosya_icerigi.split("\n")

    for i in kelimeler:
        i = list(i)
        liste.append(i[0])
    print("".join(liste))