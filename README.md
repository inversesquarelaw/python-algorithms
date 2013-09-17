python-algorithms
=================

## Overview
A bunch of random / useful algorithms in python. Designed to be short and simple to read and get a sense of how they work. These are not production ready and are aimed to represent the core structure of the algorithm.

## Insertion Sort
* **Worst Case**: O(n^2)
* **Average Case**: O(n^2)
* **Best Case**: O(n)
* **Worst Case Space**: O(n), O(1) auxiliary (actually needed seperately)
Insertion sort is adaptive (meaning efficient for data sets that are partially
sorted) the time complexity is O(n +d) where d in the number of inversions (
a pair of places of a sequence where th elements are out of order). It is
also stable (doesn't change relative order of elements), in-place (no need
for memory allocation or extra space) and Online (can sort lists as it
receives it).

## Merge Sort
* **Worst Case**: O(nlogn)
* **Average Case**: O(nlogn)
* **Best Case**: O(nlogn)
* **Worst Case Space**: O(n), O(n) auxiliary (actually needed seperately)
Merge sort has a great worst case for a stable sort (however quick sort only
has terrible preformance in contrived examples and with a random pivot we can
make it less vunerable to attack). This is the classic example of a divide
and conqure algorithm. We start with all lists seperate and combine them
inserting them in correct order, we repeat till we have 1 list in order.

## Quick Sort
* **Worst Case**: O(n^2) (extremely rare)
* **Average Case**: O(nlogn)
* **Best Case**: O(nlogn)
* **Worst Case Space**: O(n), O(logn) auxiliary (actually needed seperately)
Quicksort benefits from sequential accesses that work well with cache lines
in modern CPU architectures. The queries to memory are often localised
improving cache hits which is why it is often prefered over merge sort. You
can also do it in place and the logn extra memory is used on the stack, I
didn't bother doing that in this implementation. A random pivot is a good
measure to protect against the contrived / extremely rare cases that
quicksort exhibits O(n^2) preformance.

## Radix Sort Least Significant Digit
* **Worst Case**: O(kn)
* **Worst Case Space**: O(k + n)
Radix sort sorts data with integer keys by grouping keys by the individual
digits which share the same significant position and value. LSD starts by
taking the least significant digit and then ordering it, then the next and
so forth. Essentially it factors in the number of digits in your integer
which is a pretty awesome hack around the typical ways of sorting.

## Heap Sort
* **Worst Case**: O(nlogn)
* **Average Case**: O(nlogn)
* **Best Case**: O(nlogn)
* **Worst Case Space**: O(n), O(1) auxiliary (actually needed seperately)
This is cool because its space complexity is constant meaning it is an
in-place sort but it isn't a stable sort as it can reorder relative positions.
Generally it fails to be as efficient as quick sort but does have a better
lower bound.

## Bucket Sort
* **Worst Case**: O(n^2)
* **Average Case**: O(n + k)
* **Worst Case Space**: O(n), O(n.k) auxiliary (actually needed seperately)
Bucket sort partitions the array into k buckets, each bucket is then sorted
individually either with some sorting algorithm or by utilizing a recursive
bucket sort. It is a cousin of radix sort. The most interesting bit is the
scattering, where you can utilize bucket ranges to do a lot of interesting
things outside of just bucket sort. Maybe sorting things sort of in order
is good enough or in order to some granularity.
