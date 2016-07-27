def _get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
     
    for i in range(r + 1):
        m[0][i] = i

    return m

def change_making(coins, n):
    m = _get_change_making_matrix(coins, n)

    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            if coins[c - 1] == r:
                m[c][r] = 1

            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]

            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c - 1][r - coins[c - 1]])

    return m[-1][-1]

def main():
    print("coins?")
    coins = raw_input()
    coins = list(coins)
    print("how much change?")
    n = raw_input()
    n = int(n)

    print(change_making(coins, n))

    return

if __name__ == "__main__":
    main()
