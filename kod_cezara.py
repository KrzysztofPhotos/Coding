# SZYFR CEZARA

dlugosc = len(text)
wynik = []
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def szyfruj():
    text = str(input("Wpisz text do zaszyfrowania: "))

    for i in text:
        if str(i)  == " ":
            wynik.append(" ")
        else:
            index = alfabet.index(i)
            index = int(index) + 3
            if index > 25:
                index = index - 26
            wynik.append(alfabet[index])

def odszyfruj():
    text = str(input("Wpisz text do odszyfrowania: "))
    for i in text:
        if str(i)  == " ":
            wynik.append(" ")
        else:
            index = alfabet.index(i)
            index = int(index) + 3
            if index > 25:
                index = index - 26
            wynik.append(alfabet[index])


print("Szyfruj -> 1\nOdszyfruj -> 2")
ask = input("")

if ask.isdigit():
    if int(ask) == 1:
        szyfruj()
    elif int(ask) == 2:
        odszyfruj()


print(wynik)
