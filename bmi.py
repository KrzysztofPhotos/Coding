
# oblicz wskaźnik BMI
# 18.5  < BMI < 24.9
# wzór (wzrost w metrach np. 1.7):
# bmi = masa / (wzrost * wzrost)
#
# Oblicz BMI według powyższego wzroru dla dowolnej wagi i dowolnego wzrostu
# np. waga: 70 kg oraz 1.75 m (175 cm) wzrostu

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = round((weight / height**2),2)

if bmi <= 18.5:
    print("You are underweight.")
elif  18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")