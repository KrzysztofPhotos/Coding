

def words_dict():
    file = open("en_words.txt", "r")

    result_dict = {}

    for elements in file:

        lenEl = len(elements)
        if lenEl > 18:
            result_dict[elements] = lenEl
    return result_dict


words_dict()

def words_length_dict():
    file = open('en_words.txt', 'r')

    # define a dict to save results
    result_dict = {}

    for element in file:
        elementEl = len(element)

        if elementEl > 18:
            result_dict[elementEl] = element
    return result_dict

def car_1():
    car = {
        'brand': 'Ford',
        'Model': 'Mustang',
        'year': 1964,
        'color': 'Red',
        'price': 30000,
        'km': 89000,
        'motor': 1.6
    }


# QUESTION 4 FROM QUIZ_DICTIONARY