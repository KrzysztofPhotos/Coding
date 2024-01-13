
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

tab_check = []
for letter in chosen_word:
    tab_check.append(letter)

print(display)

counter = 0

while True:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    #print(str(display))
    #print(tab_check)
    counter += 1
    if display == tab_check:
        print('Congrats')
        break
    
print("You provided " + str(counter) + " letters")