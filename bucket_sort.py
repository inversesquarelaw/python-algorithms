def bucket_sort(iterable):
    if not iterable: return iterable
    buckets = [0] * len(iterable)
    for e in iterable: buckets[e] += 1
    out_iterable = []
    for n, acc in enumerate(buckets):
        out_iterable.extend([n]*acc)
    return out_iterable

#print bucket_sort([2,2,6,1, 1, 1 ,1 ,1])

from collections import defaultdict, Counter

# Generic for any partition definition.
def partition(iterable, key):
    d = defaultdict(list)
    for e in iterable:
        d[key(e)].append(e)
    return d

def bucket_sort_sparse(iterable):
    if not iterable: return iterable
    return sum([[k]*v for k,v in sorted(Counter(iterable).iteritems())], [])

print bucket_sort_sparse([9,2,1,4, 4])
