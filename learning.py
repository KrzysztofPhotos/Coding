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