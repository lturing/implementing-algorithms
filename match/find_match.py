# S, T is consisted of a-z lower alphabet, and find ...
'''
S = 'ababcb'
T = 'xyx'
rt: ans = 3

i = 0 # index for s
j = 0 # index for t
a map to x, b map to y, a map to x , ans += 1

i = 1
j = 0
b map to x, a map to y, b map to x, ans += 1

i = 2 
j = 0 
a map to x, b map to y, c map to x, failed, for 'a' haved been mapped to x.

i = 2

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

def match_by_kmp(S, T):
    len_s = len(S)
    len_t = len(T)

    if len_t > len_s:
        return 0 

    ans = 0 
    i = 0 
    nex = compute_skip(T)
    
    while i < (len_s-len_t+1):
        rec = {}
        flag = 0 

        j = 0 
        while j < len_t:
            #print('j=', j, 'j+i=', j+i, 'i=', i, rec)
            if T[j] not in rec or rec[T[j]] == S[i+j]:
                
                rec[T[j]] = S[j+i]
                j += 1

            elif rec[T[j]] != S[i+j]:
                i = i + nex[j-1]+1
                j = nex[j-1] + 1

                if i > len_s-len_t:
                    print('i=', i)
                    break 

                rec = {}
                for k in range(j):
                    rec[T[k]] = S[i+k]

        if j == len_t:
            ans += 1

        i += 1
    print(ans)

## version_2 
def match(S, T):
    len_t = len(T)
    len_s = len(S)
    if len_t > len_s:
        return 0 
    else:
        ans = 0
        i = 0
        while i < (len_s - len_t + 1):
            rec = {}
            j = 0
            while j < len_t:
                if T[j] not in rec:
                    rec[T[j]] = S[j+i]

                elif rec[T[j]] != S[i+j]:
                    break 
                j += 1

            if j == len_t:
                ans += 1

            i += 1

        print(ans)
