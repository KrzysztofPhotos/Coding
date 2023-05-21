
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

        # if i < 20:
        #     print(word)

words_dict()