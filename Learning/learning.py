cars = {
    'Audi': 'Germany',
    'Mazda': 'Japan',
    'Fiat': 'Italy',
    'Ford': 'US'
}

print(cars)

# LOOP OVER THE DICT

for car in cars.items():
    print(car)

for brand, country in cars.items():
    print(brand, ' - ', country)

for k in cars.keys():
    print(k)

for country in cars.values():
    print(country)

def count_letters(text):
    # a dict for a numbers and counts

    letters = {} # create dict

    for l in text:

        if l.isalpha():

            # check if this letter is already in dict
            if l in letters.keys():
                letters[l] += 1
            else:
                letters[l] = 1

    return letters

text = 'example text.'
print(count_letters(text))

#
# def count_letters_2(text):
#
#     letters = dict()
#     for letter in text:
#         if letter.isalpha():

def reverse_lookup(dictionary, value):

    # loop over the dictionary
    for key in dictionary:

        # check if the value with this key == value
        if dictionary[key] == value:
            # we found the key
            return key
    else:
        # raise error
        raise KeyError('We could not find with this value: ',value)

dictionary = {
    'a': 2,
    'b': 1,
    'c': 4,
    'd': 3,
    'e': 2
}

print(dictionary)

value = 2
print(reverse_lookup(dictionary, value))

value = 122
print(reverse_lookup(dictionary, value))

# LIST CAN BE USED AS VALUES IN DICTIONARIES

def list_of_letters(text):
    # get the dictionary of occurences
    dictionary = count_letters(text)

    letters = {}

    for key in dictionary:

        # get value
        value = dictionary[key]

        # if this value is in keys -> add it and assing a list of key
        if value not in letters:
            letters[value] = [key]
        else:
            # this value is in letters keys
            letters[value].append(key)
    return letters

text = 'example text!'
print(list_of_letters(text))


def words_dict():
    file = open('en_words.txt')
    for elements in file:
        print(elements)

