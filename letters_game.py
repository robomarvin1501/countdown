"""
https://github.com/dwyl/english-words <- Where the words are from
Use words_alpha.txt
"""
import sys

countdown = True

with open("all_words.txt", 'r') as f1:
    words_list = f1.read()

words_list = words_list.replace('\n', ' ')
words_list = words_list.split()
words = dict()

for x in range(len(words_list)):
    words[''.join(sorted(words_list[x]))] = words_list[x]


def quant_str(s):
    data = dict()
    for x in s:
        if x not in data:
            data[x] = 0
        data[x] += 1
    return data


def check_str(part, full):
    part = quant_str(part)
    full = quant_str(full)

    for x in part.keys():
        if x not in full:
            return False
        else:
            if part[x] > full[x]:
                return False

    return True


def play():
    letters = input("Letters: ")
    if ' ' in letters:
        sys.exit()
    letters = ''.join(sorted(letters))

    out = []
    for x in words.keys():
        if check_str(x, letters):
            if countdown:
                if len(words[x]) <= 9:
                    out.append(words[x])
            else:
                out.append(words[x])

    out.sort(key=len, reverse=True)
    print(out[:10])


if __name__ == "__main__":
    while True:
        play()
