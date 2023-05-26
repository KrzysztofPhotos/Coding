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