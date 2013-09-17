from heapq import merge

def merge_sort(iterable):
    if len(iterable) <= 1: return iterable
    middle = int(len(iterable)/2)
    lhs = merge_sort(iterable[:middle])
    rhs = merge_sort(iterable[middle:])
    return list(merge(lhs, rhs))
