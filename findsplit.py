import sys
import enchant
d = enchant.Dict("en_US")

def find_possibilities(string):
    possibilities = []
    for n in range(2, len(string) + 1):
        possibility = string[:n]
        if d.check(possibility):
            possibilities.append(possibility)

    print(possibilities)
    return possibilities

def find_score(split):
    total = 0
    for word in split:
        total += get_score(word)

    return total

def get_score(string):
    return len(string)**2

def find_split(string, score):
    if string == "":
        return score

    possibilities = find_possibilities(string)
    minimum = sys.maxint

    for possibility in possibilities:
        poss_score = get_score(possibility)
        poss_score = find_split(string[len(possibility):], poss_score + score)
        minimum = min(poss_score, minimum)

    return minimum

def main():
    sentence = raw_input()
    print(find_split(sentence, 0))

if __name__ == "__main__":
    main()
