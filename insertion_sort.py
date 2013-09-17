def insertion_sort(iterable):
    if not iterable: return iterable

    for i in xrange(1, len(iterable)):
        j, key = i - 1, iterable[i]
        while (iterable[j] > key and j >= 0):
            iterable[j+1] = iterable[j]
            j -= 1
        iterable[j+1] = key
    return iterable

print insertion_sort([9,2,1,5])

import bisect

def insertion_binary(iterable):
    for i in range(1, len(iterable)):
        bisect.insort(iterable, iterable.pop(i), 0, i)
