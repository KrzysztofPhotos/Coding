t = 'x', 'y', 'z', 'q', 'p'

print(type(t))

print(isinstance(t, tuple))
print(isinstance(t, list))

one_tuple = 'x',

print(type(one_tuple))

single = tuple('x')
print(type(single))

lang = tuple("Python")
print(lang)

print(lang[0])
print(lang[1])

my_list = ["A", "B", "C", "D"]
list_tuple = tuple(my_list)

print(list_tuple)

text = "Moon is the orbit of Earth"

tup = tuple(text)

print(tup)

# slicing
# the word -> Moon
print(tup[0:4])
print(tup[-5:])

duplicate = tup[::]

print(duplicate)

print("a" > "b")

