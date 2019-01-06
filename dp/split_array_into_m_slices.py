'''
for Segmental CRF
SCRF is a variant of the linear-chain CRF model where each output token corresponds to a segment of input tokens instead of a single input instance.
[multitask learning with ctc and segmental crf for speech recognition](https://arxiv.org/pdf/1702.06378.pdf)
'''
import copy 

# split an array of lenght n into m slices
'''
n = input()
m = input()
'''

n = 30
m = 4

assert n >= m, "n must be not less than m"

f = {}

def traverse_split(n=n, m=m):
    if (n, m) not in f:
        f[n, m] = 0
    if m == 1:
        f[n, m] = 1
        return 
    for i in range(n-1, max(m-2, 0), -1):
        if (i, m-1) not in f:
            traverse_split(i, m-1)
        f[n, m] += f[i, m-1]

'''
traverse_split()
print(f[n, m])
'''

f = {}
def traverse_split_rec(n=n, m=m):
    if m == 1:
        f[n, m] = [[n]]
        return 
    if (n, m) not in f:
        f[n, m] = []

    for i in range(n-1, max(m-2, 0), -1):
        if (i, m-1) not in f:
            traverse_split_rec(i, m-1)
            
        tmp = copy.deepcopy(f[i, m-1])
        for item in tmp:
            item.append(n)
            f[n, m].append(item)

traverse_split_rec()
ret = f[n, m]
ret = sorted(ret, key=lambda asd:([asd[i] for i in range(len(asd))]))

for item in ret:
    tmp = ''
    j = 0 
    for i in range(0, n):
        if i < item[j]:
            tmp += str(i+1) + ' '
        else:
            tmp = tmp[:-1] + ', ' + str(i+1) + ' '
            j += 1

    print(tmp)
