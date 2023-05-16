lines = []

with open("przyklad.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

moj_napis = []
for i in lines:
    #print(i)
    z = i.split()
    if z[0] == "DOPISZ":
        moj_napis.append(str(z[1]))
    elif z[0] == "USUN":
        moj_napis.pop()
    elif z[0] == "ZMIEN":
        moj_napis.pop()
        moj_napis.append(str(z[1]))
    elif z[0] == "PRZESUN":

        # szukamy miejsca które jest do zmiany
        miejsce = len(moj_napis)-1
        for m in range(len(moj_napis)):
            od_ostatniego = len(moj_napis)-m-1

            miejsce -= 1
            if moj_napis[od_ostatniego] == z[1]:
                break
            #miejsce -= 1

        if ord(z[1])+1 > 90:
            nowa_liczba = chr(ord(z[1]) + 1 - 26)
        else:
            nowa_liczba = chr(ord(z[1])+1)

        moj_napis[miejsce] = nowa_liczba


        # index = len(moj_napis)-1
        #
        # while str(moj_napis[index]) != str(z[1]):
        #     index -= 1
        #
        # print(index)
        #
        # if ord(z[1])+1 > 90:
        #     nowa_liczba = chr(ord(z[1]) + 1 - 26)
        # else:
        #     nowa_liczba = chr(ord(z[1])+1)
        #
        # moj_napis[index] = nowa_liczba


#print(moj_napis)

# całkowita długość napisu
napis_dlugosc = len(moj_napis)

s = open("wynik4.txt", "w")

s.write("4.1 " + str(napis_dlugosc))

napis = ""
for i in moj_napis:

    napis += i
s.write("\n\n4.4 " + str(napis))


count = 0
przewaga = ""

for i in lines:
    linia = i.strip()


