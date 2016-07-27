import numpy as np

def main():
    print(naive(20, 30))
    pass

def naive(turns, tiles):
    print(turns, tiles)
    return naive_recursive(turns, 0, tiles)
    pass

def naive_recursive(turn, position, tiles):
    if position < 0:
        return 0
    if turn == 0:
        if position == tiles - 1:
            return 1
        else:
            return 0
    else:
        return (naive_recursive(turn - 1, position - 1, tiles) +
                naive_recursive(turn - 1, position, tiles) +
                naive_recursive(turn - 1, position + 1, tiles))
    pass

if __name__ == "__main__": main()
