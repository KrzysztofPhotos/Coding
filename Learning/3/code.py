lines = []
with open("en_words.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

dictionary = {}
dictionary2 = {}
def words_dict(word):
    if len(word) >= 19:
        dictionary[word] = len(word)
def words_len_dict(word):
    if len(word) >= 19:
        dictionary2[len(word)] = word

for word in lines:
    words_dict(word)
    words_len_dict(word)

print(dictionary)
print(dictionary2)

def car_1():
    car = {}

    car['brand'] = 'Ford'
    car['model'] = 'Mustang'
    car['year'] = 1964
    car['color'] = 'Red'
    print(car)

car_1()

def car_2():
    car = {}
    car.update({car['brand']: 'Ford',
    car['model']: 'Mustang',
    car['year']: 1964,
    car['color']: 'Red'})
    print(car)

car_2()
print("Q3 --------------")

def create_a_new_car():
