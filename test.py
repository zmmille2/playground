from collections import defaultdict
something = open("tty.txt", "r").read().split("\n")
doh = defaultdict(int)

for thing in something:
    doh[thing] += 1

for key in doh.keys():
    if doh[key] != 2:
        print key
