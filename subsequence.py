def longest_increasing_subsequence(sequence, highest):
    if len(sequence) == 1 or len(sequence) == 0:
        if int(sequence) < highest:
            return sequence
        return ""
    a = longest_increasing_subsequence(sequence[:len(sequence) - 1], highest)
    print("a = " + a)
    if int(sequence[len(sequence) - 1]) < highest:
        b = longest_increasing_subsequence(sequence[:len(sequence) - 1], sequence[len(sequence) - 1]) + str(sequence[len(sequence) - 1])
    else:
        b = ""
    print("b = " + b)

    if a > b:
        return a
    return b

def main():
    sequence = raw_input()
    sequence = sequence.replace(" ", "")
    print longest_increasing_subsequence(sequence, 10)

if __name__ == "__main__":
    main()
