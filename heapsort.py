from heapq import heappush, heappop

def heapsort(iterable):
    heap = []
    for e in iterable: heappush(heap, e)
    return [heappop(heap) for i in xrange(len(heap))]

print heapsort([1, 9,2,4])
