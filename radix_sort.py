def radix_sort(iterable, num_buckets, max_length):
    for digit in xrange(max_length):
        buckets = [[] for j in xrange(num_buckets)]
        for e in iterable:
            buckets[(e/10**digit)%num_buckets].append(e)
        iterable = sum(buckets, [])
    return iterable

print radix_sort([10, 9, 15, 25], 10, 3)
