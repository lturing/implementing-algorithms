# 将一个数组分成两部分，使每部分的和相差最小
import random

def split_list(data):
    n = len(data)
    data = sorted(data)
    asum = sum(data)//2+1 

    dp = []
    amax = 0 
    for i in range(1+n):
        dp.append([])
        dp[-1] = [0]*asum

    for i in range(1, 1+n):
        for v in range(data[i-1], asum):
            dp[i][v] = max(dp[i-1][v], dp[i-1][v-data[i-1]]+data[i-1])
            amax = max(dp[i][v], amax)

    ans = [0]*n 

    for i in range(n, 0, -1):
        if dp[i][amax] > dp[i-1][amax]:
            amax -= data[i-1]
            ans[i-1] = 1

    a = []
    b = []
    for i in range(n):
        if ans[i] == 0:
            a.append(data[i])
        else:
            b.append(data[i])

    print('a=', a)
    print('b=', b)


data = [random.randint(10, 100) for i in range(4)]

split_list(data)
