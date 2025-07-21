"""
https://github.com/dwyl/english-words <- Where the words are from
Use words_alpha.txt
"""
import sys
from itertools import permutations

countdown = True

with open("all_words.txt", 'r') as f1:
    words_list = f1.read()

words_list = words_list.replace('\n', ' ')
words_list = words_list.split()
words = dict()

'''
for x in words_list:
    nine = x
    eight = ''.join([''.join(sec) for sec in list(permutations(x, 8))])
    seven = ''.join([''.join(sec) for sec in list(permutations(x, 7))])
    six = ''.join([''.join(sec) for sec in list(permutations(x, 6))])
    five = ''.join([''.join(sec) for sec in list(permutations(x, 5))])
    four = ''.join([''.join(sec) for sec in list(permutations(x, 4))])

    every_iter = nine + eight + seven + six + five + four

    words[x] = every_iter
'''


for x in range(len(words_list)):
    words[''.join(sorted(words_list[x]))] = words_list[x]


while True:
    letters = input("Letters: ")
    if ' ' in letters:
        sys.exit()
    letters = ''.join(sorted(letters))
    # letters += ''.join(sorted([''.join(sec) for sec in list(permutations(letters, 8))]))
    # letters += ''.join(sorted([''.join(sec) for sec in list(permutations(letters, 7))]))
    # letters += ''.join(sorted([''.join(sec) for sec in list(permutations(letters, 6))]))
    # letters += ''.join(sorted([''.join(sec) for sec in list(permutations(letters, 5))]))
    # letters += ''.join(sorted([''.join(sec) for sec in list(permutations(letters, 4))]))

    print("+++SORTED LETTERS+++")

    out = []
    for x in words.keys():
        if x in letters:
            if countdown:
                if len(words[x]) <= 9:
                    out.append(words[x])
            else:
                out.append(words[x])

    out.sort(key=len, reverse=True)
    print(out[:10])
