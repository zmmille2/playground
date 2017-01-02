from collections import defaultdict

#4918
num_elves = 3001330
elves = []

class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = self

    def remove_next(self, num_elves):
        self.nxt = self.nxt.nxt
        return num_elves - 1

def before_cross_elf(index):
    return (index + ((num_elves) / 2) - 1) % num_elves

root = Node(1)
curr = root

for elf in range(2, num_elves + 1):
    curr.nxt = Node(elf)
    curr = curr.nxt

curr.nxt = root
curr = root
curr_cross = curr

i, curr_index, cross_index = 0, 0, (num_elves / 2 - 1)

while cross_index > i:
    curr_cross = curr_cross.nxt
    i += 1

while num_elves > 1:
    before_cross = before_cross_elf(curr_index)
    while cross_index != before_cross:
        curr_cross = curr_cross.nxt
        cross_index = (cross_index + 1) % num_elves
    if curr.value == curr_cross.nxt.value:
        num_elves = curr.remove_next(num_elves)
    else:
        num_elves = curr_cross.remove_next(num_elves)
    cross_index %= num_elves
    curr = curr.nxt
    if curr_index > num_elves:
        curr_index = 0
    else:
        curr_index = (curr_index + 1) % (num_elves + 1)

print curr.value
