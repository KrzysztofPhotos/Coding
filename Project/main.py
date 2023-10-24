sciezka = str(input("Enter folder location:"))

import os


# Inicjalizacja licznika elementów
licznik_elementow = 0
# Przeszukiwanie katalogu
for element in os.listdir(sciezka):
    pelna_sciezka = os.path.join(sciezka, element)
    if os.path.isfile(pelna_sciezka) or os.path.isdir(pelna_sciezka):
        licznik_elementow += 1

print(f"Liczba elementów w katalogu {sciezka}: {licznik_elementow}")


for element in os.listdir(sciezka):
    pelna_sciezka = os.path.join(sciezka, element)
    if os.path.isfile(pelna_sciezka):
        #print(element)
        rozszerzenie = element.split(".")[-1]
        print("Rozszerzenie pliku:", rozszerzenie)
