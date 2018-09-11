left = lambda i: 2*i+1
right = lambda i: 2*i+2

def heapify(alist, i):
    l, r = left(i), right(i)
    largest = l if l < heap_size and alist[i] < alist[l] else i 
    largest = r if r < heap_size and alist[largest] < alist[r] else largest 

    if i != largest:
        alist[i], alist[largest] = alist[largest], alist[i]
        heapify(alist, largest)

def build_max_heap(alist):
    global heap_size
    heap_size = len(alist)
    for i in range(heap_size//2, -1, -1):
        heapify(alist, i)

def heapsort(alist):
    global heap_size 
    build_max_heap(alist)
    for i in range(len(alist)-1, -1, -1):
        alist[i], alist[0] = alist[0], alist[i]
        heap_size -= 1
        heapify(alist, 0)

alist = [1, 2, 3, 4, 5, 6, 6, 5, 8, 3]
heap_size = 0 

heapsort(alist)
print(alist)
