import scrabble
import string

vowels = 'aeiou'

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

# print words that contain all vowels
for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)

# #print all letters that never appear doubled
# for letter in string.ascii_lowercase:
#     exists = False
#     for word in scrabble.wordlist:
#         if letter * 2 in word:
#             exists = True
#             break
#     if not exists:
#         print("There are no English words with a double " + letter)

# #print all words containing "uu"
# for word in scrabble.wordlist:
#     if "uu" in word:
#         print(word)