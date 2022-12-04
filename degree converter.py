
print("Welcome in Degree Converter")

ask = int(input("Tell me which value do you wanna get?\nType 1 -> convert celcius to farenheit\nType 2 -> convert farenheit to celcius\n"))
val = float(input("Type here a value to convert: "))

if ask == 1: # F -> C
    print("\n*** Converted result ***\nThe", val, "°F is equal to ", round((val - 32) * 5/9, 1), "°C")
elif ask == 2: # C -> F
    print("\n*** Converted result ***\nThe", val, "°C is equal to ", round(val * 9/5 + 32, 1), "°F")
else:
    print("Incorrect value.")
