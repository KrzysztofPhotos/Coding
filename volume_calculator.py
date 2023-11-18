# Program to calculate the volume/area of a sphere, cube, pyramid, etc.

# AREAS FUNCTIONS

def square_area(a):
    return int(a)**2

def rectangle_area(a, b):
    return int(a) * int(b)

def triangle_area(a, h):
    return int(a) * int(h) / 2

def circle_area(r):
    return str(float(r)**2) + "π"

def trapezoid_area(a, b, h):
    return ((a + b) * h) / 2

def rhombus_area(a, h):
    return a * h

def parallelogram_area(a, h):
    return a * h

# VOLUME FUNCTIONS

def cube_volume(a):
    return a**3

def rectangular_prism_volume(l, w, h):
    return l * w * h

def triangular_prism_volume(b, h, H):
    return b * h * H / 2

def cylinder_volume(r, h):
    return str((r**2) * h) + "π"

def cone_volume(r, h):
    return str((r**2) * h / 3) + "π"

def sphere_volume(r):
    return str(4/3 * (r**3)) + "π"

def pyramid_volume(a, b, h):
    return a * b * h / 3

print("Welcome to the calculator!\n")
operation = input("Please select which operation do you want to do:\n1) Area Calculator\n2) Volume Calculator\n...")

if operation == "1":
    operation2 = input("Select what area you want to calculate: ")

    if operation2 == "1":
        side = input("Give the length of the side of the square: ")
        print("The square area of a square with side length " + str(side) + " is = " + str(square_area(side)))

    if operation2 == "2":
        side1 = input("Give the length of the FIRST side of the rectangle: ")
        side2 = input("Give the length of the SECOND side of the rectangle: ")
        print("The area of " + str(side1) + "x" + str(side2) + " rectangle is = " + str(rectangle_area(float(side1), float(side2))))

    if operation2 == "3":
        base = input("Give the base length of the triangle: ")
        height = input('Give the height of the triangle: ')
        print("The area of a triangle with base " + str(base) + " and height " + str(height) + " is = " + str(triangle_area(float(base), float(height))))

elif operation == "2":
    operation2 = input("Select what volume you want to calculate: ")

    if operation2 == "1":
        side = input("Give the length of the side of the cube: ")
        print("The volume of a cube with side length " + str(side) + " is = " + str(cube_volume(float(side))))

    if operation2 == "2":
        length = input("Give the length of the rectangular prism: ")
        width = input("Give the width of the rectangular prism: ")
        height = input("Give the height of the rectangular prism: ")
        print("The volume of a rectangular prism with dimensions " + str(length) + "x" + str(width) + "x" + str(height) + " is = " + str(rectangular_prism_volume(float(length), float(width), float(height))))

    if operation2 == "3":
        base = input("Give the length of the base of the triangular prism: ")
        height_base = input("Give the height of the base triangle: ")
        height_prism = input("Give the height of the triangular prism: ")
        print("The volume of a triangular prism with base dimensions " + str(base) + "x" + str(height_base) + " and height " + str(height_prism) + " is = " + str(triangular_prism_volume(float(base), float(height_base), float(height_prism))))

    if operation2 == "4":
        radius_cylinder = input("Give the radius of the cylinder: ")
        height_cylinder = input("Give the height of the cylinder: ")
        print("The volume of a cylinder with radius " + str(radius_cylinder) + " and height " + str(height_cylinder) + " is = " + str(cylinder_volume(float(radius_cylinder), float(height_cylinder))) + " cubic units")

    if operation2 == "5":
        radius_cone = input("Give the radius of the cone: ")
        height_cone = input("Give the height of the cone: ")
        print("The volume of a cone with radius " + str(radius_cone) + " and height " + str(height_cone) + " is = " + str(cone_volume(float(radius_cone), float(height_cone))) + " cubic units")

    if operation2 == "6":
        radius_sphere = input("Give the radius of the sphere: ")
        print("The volume of a sphere with radius " + str(radius_sphere) + " is = " + str(sphere_volume(float(radius_sphere))) + " cubic units")

    if operation2 == "7":
        base_pyramid = input("Give the length of the base of the pyramid: ")
        height_pyramid = input("Give the height of the pyramid: ")
        print("The volume of a pyramid with base length " + str(base_pyramid) + " and height " + str(height_pyramid) + " is = " + str(pyramid_volume(float(base_pyramid), float(height_pyramid))) + " cubic units")

else:
    print("Error!")
