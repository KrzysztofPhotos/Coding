word_list = ['police', 'buzzard', 'lucky', 'jackpot', 'wall', 'stronghold', 'icebox', 'luxury', 'microwave', 'fake', 'oxygen', 'matrix']
# add a possibility to change the category of words for instance:
# - animals
# - technology
# - food
# - other
# - etc

import random
import time

# **** NEW VERSION**** #

chosen_word = random.choice(word_list)

answer = []
for i in range(len(chosen_word)):
    answer.append("_")
    
hearts1 = 5
print(answer)



def main_code():
    hearts = hearts1
    guess = input("Guess a letter: ").lower()

    h = 0
    counter = 0
    for letter in chosen_word:
        if letter == guess:
            h = 1
            answer[counter] = letter
        else: 
            print("not good")
        counter += 1
    
    if h == 0:
        hearts -= 1
            
    print(chosen_word)

    print("\nanswer")
    print(answer)
    
    if str(chosen_word) == str(answer):
        print('CONGRAATSSS')
        print(chosen_word)
        print(answer)
    
    print("Ilosc serc: " + str(hearts))
    
    if hearts > 0:
        main_code()

# ***** ***** **** **** **** **** **** #
main_code()

# word_to_guess_str = word_list[random.randint(0, len(word_list)-1)]

# hearts = 5

# word = []
# for i in word_to_guess_str:
#     word.append(i)

# print(word) # DEBUG TOOL

# print("_ " * len(word_to_guess_str))

# while hearts > 0:

#     time.sleep(1)
#     letter_input = input("Guess a letter: ")

#     for i in range(len(word)):
#         if letter_input == word[i]:
#             print("success")

#             #now we need to print _ _ _ _ _ _ with lettters
#             # for example _ a _ a _ _ and save it to variable
#         else:
#             print("wrong letter" + " HEARTS: " + str(hearts))
#             hearts -= 1

