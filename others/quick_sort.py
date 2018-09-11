# https://en.wikipedia.org/wiki/Quicksort

def partition(alist, start, end):
    x = alist[end]
    i = start - 1
    for j in range(start, end):
        if alist[j] <= x:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]

    alist[i+1], alist[end] = alist[end], alist[i+1]

    return i+1 

def quick_sort_asc(alist, start, end):
    if start < end:
        pivot = partition(alist, start, end)
        quick_sort_asc(alist, start, pivot-1)
        quick_sort_asc(alist, pivot+1, end)


alist = [1, 2, 3, 4, 5, 6, 6, 5, 8, 3]
start = 0 
end = len(alist)-1

quick_sort_asc(alist, start, end)
print(alist)
