# program to calculate the volume/area of sphere, cube or pyramid etc.



def volume_calculator():
    print("Calculate the volume of\n1) Sphere\n2) Cube\n3) Pyramid\n4) Cuboid")

def area_calculator():
    print("\nCalculate the area of\n1) Square\n2) Cube\n3) Pyramid\n4) Cuboid")
    operation2 = input("I want to calculate: ")

    if operation2 == 1:
        side = int(input("Type the lenght of the side:"))
        print(rectangle_area(int(side),int(side)))
    #elif operation2 == 2:

def rectangle_area(a, b):
    return a*b


print("Welcome to volume and area calculator!\nPlease select which operation do you wanna do:")
operation = input("Calculate\n1) Area\n2) Volume")

if operation == "1":
    area_calculator()
#elif operation == 2:
    
else:
    print("Error! Incorrect value!")