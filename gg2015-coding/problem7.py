from collections import defaultdict

def main():

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    cypher = open('cypher')
    text = cypher.readlines()
    possibilities = defaultdict(lambda : defaultdict(string))

    for letter in alphabet:
        print letter 

if __name__ == "__main__": main()
