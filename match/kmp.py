# ./../paper/kmp.pdf

def compute_skips(P):
    nex = {}
    nex[1] = 0 # not include the current pos [0, 1, ..., i-1]
    i = 1
    j = 0
    n = len(P)

    while i < n:
        if P[i] == P[j]:
            i += 1
            j += 1
            nex[i] = nex[i-1]+1
            #nex[i] = j 

        elif j > 1:
            j = nex[j-1]

        if j == 0:
            i += 1 
            nex[i] = 0 
    
    return nex 

def kmp(S, P):
    nex = compute_skips(P)
    i = 0 # index for S
    j = 0 # index for P
    s_len = len(S)
    p_len = len(P)
    while i < s_len:
        if S[i] == P[j]:
            i += 1
            j += 1
            if j == p_len:
                print(i-j, S[i-j:i])
                j = nex[j] # great 

        elif j == 0:
            i += 1
        else:
            j = nex[j] 

S = 'BBC ABCDAB ABCDABCDABDE'*7
P = 'ABCDABD'

kmp(S, P)

# version_2
'''
def compute_skip(P):
    nex = {}
    i = 0 
    j = 0 
    nex[i] = 0 # include current pos
    p_len = len(P)
    while (i+1) < p_len:
        if P[i+1] == P[j]:
            i += 1
            j += 1
            nex[i] = j 
        elif j == 0:
            i += 1
            nex[i] = 0 
        else:
            j = nex[j-1] 

    return nex 

def kmp(S, P):
    nex = compute_skip(P)
    i = 0 
    j = 0 
    s_len = len(S)
    p_len = len(P)

    while i < s_len:
        if S[i] == P[j]:
            i += 1
            j += 1
            if j == p_len:
                j = nex[j-1]

        elif j == 0:
            i += 1
        else:
            j = nex[j-1]

S = 'BBC ABCDAB ABCDABCDABDE'*7
P = 'ABCDABCD'

kmp(S, P)
'''
