a = int(input("First number: "))
b = int(input("Second number: "))

try:
    c = a/b
except:
    c = None
    print("There was an error")
    
print(c)