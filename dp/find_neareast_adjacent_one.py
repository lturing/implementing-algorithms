import random 

def find_near_adjacent_one_exclude(lens=20):
    data = [1 if random.random() > 0.7 else 0 for _ in range(lens)]

    ans = [float('inf')]

    last = None 
    if data[0] == 1:
        last = 0 

    for i in range(1, len(data)):
        if last == None:
            ans.apepnd(float('inf'))
        else:
            ans.append(i-last)

        if data[i] == 1:
            last = i 

    last = None 
    if data[-1] == 1:
        last = len(data) - 1

    for i in range(len(data)-2, -1, -1):
        if last != None:
            ans[i] = min(ans[i], last-i)

        if data[i] == 1:
            last = i 

    print(data)
    print(ans)

def find_near_adjacent_oen_include(lens=20):
    data = [1 if random.random() > 0.7 else 0 for _ in range(lens)]

    ans = [float('inf')]
    if data[0] == 1:
        ans[0] = 0 

    for i in range(1, lens):
        if data[i] == 1:
            ans.append(0)
        else:
            ans.append(ans[-1]+1)
            '''
            if ans[-1] == float('inf'):
                ans.append(float('inf'))
            else:
                ans.append(ans[-1] + 1)
            '''

    for i in range(lens-2, -1, -1):
        ans[i] = min(ans[i], ans[i+1]+1)
    
    print(data)
    print(ans)
    
