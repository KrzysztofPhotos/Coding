
MIN_CHAR_LENGTH = 19


def words_dict():

    # an empty dict
    dictionary = {}

    # read the words
    file = open('en_words.txt')

    # iterate over file -> line by line
    for i, line in enumerate(file):

        # line -> \n
        line_list = line.split()

        word = line_list[0]

        if len(word) >= MIN_CHAR_LENGTH:
            print(word)


        # add the word into the dict
        dictionary[len(word)] = word

words_dict()