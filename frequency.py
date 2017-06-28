from collections import defaultdict
import pdb

class Solution(object):
    def push_index(self, heap, key, index, frequency):
        value = frequency[key]
        if heap == []:
            return [key], frequency
        elif frequency[heap[index]] >= value:
            # logic here is messed up: this should be true!
            print 'frequency[', heap[index], ']=', frequency[heap[index]], 'value=', value
            heap = heap[:index] + [key] + heap[index:]
            return heap, frequency
        elif index % 2 == 0:
            print 'other'
            index -= 2
            index /= 2
        else:
            print 'again, other'
            index -= 1
            index /= 2
        return self.push_index(heap, key, index, frequency)

    def push(self, heap, key, frequency):
        return self.push_index(heap, key, len(heap) - 1, frequency)

    def frequencySort(self, s):
        frequency = defaultdict(int)
        heap = []
        for letter in s:
            frequency[letter] += 1
        print frequency
        for key in frequency.keys():
            pdb.set_trace()
            heap, frequency = self.push(heap, key, frequency)
            print heap
        for key in heap[::-1]:
            for i in xrange(frequency[key]):
                print key,
        print

test = Solution()
test.frequencySort('test')
