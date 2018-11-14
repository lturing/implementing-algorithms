from fractions import Fraction
import matplotlib.pyplot as plt 
import numpy as np 
import math 


pattern = [(2, 3), (1, 3), (1, 6), (1, 12), (1, 18), (1, 21)]
pattern = [(1, 3), (1, 6), (1, 8), (1, 9)]

def min_common(a, b):
    x = a
    y = b
    while b:
        tmp = b
        b = a % b 
        a = tmp 

    if x * y % a != 0:
        print('there are some bugs to fix.')

    return x * y // a 

def get_t():
    global pattern

    T = 1 
    tset = []
    for p in pattern:
        t = Fraction(p[1], p[0]) * 2
        tset.append(str(t))
        T = min_common(T, t)

    return tset, T 


def coss(i):
    global pattern
    
    ans = 0
    for p in pattern:
        ans += math.cos(Fraction(p[0], p[1]) * math.pi * i)
    
    return ans 

def marker(idxs, arrays, plt):
    if len(idxs) < 20:
        for idx in idxs:
            y = round(arrays[idx], 3)
            plt.text(idx, y, idx, ha='center', va='bottom')

    plt.scatter(idxs, [arrays[i] for i in idxs], c='black', linewidths=0.1)


def ajust(min_heap, x, i=0):
    left = 2 * i + 1
    right = 2 * i + 2
    lens = len(min_heap)
    minest = left if left < lens and x[min_heap[left]] < x[min_heap[i]] else i 
    minest = right if right < lens and x[min_heap[right]] < x[min_heap[minest]] else minest 

    if minest != i:
        min_heap[minest], min_heap[i] = min_heap[i], min_heap[minest]
        ajust(min_heap, x, minest) 

def pltt():

    tset, T = get_t()
    repeat = 8
    total = repeat * T 
    N = total * 100
    x = [coss(i) for i in np.linspace(0, total, N)]

    max_idx = []
    min_heap = []

    for i in range(len(x)-1):
        if len(min_heap) < repeat:
            min_heap.insert(0, i)
            ajust(min_heap, x)
        elif x[min_heap[0]] < x[i]:
            min_heap[0] = i
            ajust(min_heap, x)

    max_idx = min_heap

    plt.figure(0)
    plt.plot(x)
    fun = []
    for p in pattern:
        tmp = r'\cos(\frac{%d}{%d} \pi * t)' % (p[0], p[1])
        fun.append(tmp)

    fun = r'$' + ' + '.join(fun) + r'$'

    plt.title('elementary frequence: ' + ','.join(tset) + '\n' + 'common frequnce: {0}'.format(T) + '\n' + 'repeat: {0}'.format(repeat) + '\n' + fun)
    marker(max_idx, x, plt)
    
    fft = np.fft.rfft(x)
    amp = []
    for item in fft:
        tmp = math.sqrt(math.pow(item.real, 2) + math.pow(item.imag, 2))
        amp.append(math.log(tmp))

    max_idx = []
    for i in range(len(amp)):
        if i == 0 and amp[i] > amp[i+1]:
            max_idx.append(i)
        elif amp[i-1] < amp[i] and amp[i] > amp[i+1]:
            max_idx.append(i)
    
    fig = plt.figure(1)
    plt.plot(amp)
    marker(max_idx, amp, plt)
    plt.title('sample {1} points from 0 to {0}'.format(total, N) + '\n' + 'amplitudes in log scale')
    plt.show()

pltt()
