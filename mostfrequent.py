from collections import defaultdict

counts = defaultdict(int)
maxcount = 0
maxkey = -1

for item in array:
    counts[item]++
    if counts[item] > maxcount:
        max_count = counts[item]
        max_key = item

return max_key
