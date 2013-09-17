#!/usr/bin/python

def quick_sort(iterable):
    if not iterable: return []
    pivot = iterable[0]
    lhs = quick_sort([e for e in iterable[1:] if e < pivot])
    rhs = quick_sort([e for e in iterable[1:] if e >= pivot])
    return lhs + [pivot] + rhs
