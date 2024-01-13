word_list = ['police', 'buzzard', 'lucky', 'jackpot', 'wall', 'stronghold', 'icebox', 'luxury', 'microwave', 'fake', 'oxygen', 'matrix']
# add a possibility to change the category of words for instance:
# - animals
# - technology
# - food
# - other
# - etc

import random



word_to_guess_str = word_list[random.randint(0, len(word_list)-1)]

word = []

for i in word_to_guess_str:
    word.append(i)

print(word)





#letter_input = input("Guess a letter: ")

