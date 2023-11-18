# program to calculate the volume/area of sphere, cube or pyramid etc.



# def volume_calculator():
#     print("Calculate the volume of\n1) Sphere\n2) Cube\n3) Pyramid\n4) Cuboid")

# def area_calculator():
#     print("\nCalculate the area of\n1) Square\n2) Cube\n3) Pyramid\n4) Cuboid")
#     operation2 = input("I want to calculate: ")

#     if operation2 == 1:
#         side = int(input("Type the lenght of the side:"))
#         print(rectangle_area(int(side),int(side)))
#     #elif operation2 == 2:

# def rectangle_area(a, b):
#     return a*b


# print("Welcome to volume and area calculator!\nPlease select which operation do you wanna do:")
# operation = input("Calculate\n1) Area\n2) Volume")

# if operation == "1":
#     area_calculator()
# #elif operation == 2:
    
# else:
#     print("Error! Incorrect value!")
    
    
    
# AREAS FUNCTIONS #
    
def square_area(a):
    return a*a

def rectangle_area(a, b):
    return a*b

def triangle_area(a, h):
    return a*h/2

def circle_area(r):
    return str(float(r)**2) + "π"

def trapezoid_area(a, b, h):
    return ((a+b)*h)/2

def rhombus_area(a, h):
    return a*h

def paallelogram_area(a, h):
    return a*h

# VOLUME FUNCTIONS #

def cube_volume(a):
    return a**3

def rectangular_prism_volume(l, w, h):
    return l*w*h

def triangular_prism_volume(b, h, H):
    return b*h*H/2

def cylinder_volume(r, h):
    return str((r**2)*h) + "π"

def cone_volume(r, h):
    return str((r**2)*h/3) + "π"

def sphere_volume(r):
    return str(4/3*(r**3)) + "π"

def pyramid_volume(a, b, h):
    return a*b*h/3
