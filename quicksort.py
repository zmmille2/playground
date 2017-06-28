# stolen shamelessly from:
# http://stackoverflow.com/questions/18262306/quicksort-with-python

def quicksort(array):
    less, equal, greater = [], [], []

    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + list(equal) + quicksort(greater)

print(quicksort([1,2,3,2,54,2,3432,124,54,32]))
