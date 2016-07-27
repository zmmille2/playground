from collections import defaultdict

file_data = open('file_data')
text = file_data.readlines()
hashtable = defaultdict(lambda : defaultdict(str))

for line in text:
    md5, size = line.split()
    hashtable[md5][size] = 'bunga'

print(len(hashtable))
