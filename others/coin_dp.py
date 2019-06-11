import sys

# 用指定的不限量的硬币拼凑指定的整数的种数
def cou_coin_most(num):
    dp = [0]*(num+1)
    dp[0] = 1
    coins = [1, 2, 5, 10, 20, 50, 100]
    for c in coins:
        for i in range(1, num+1):
            if i-c>=0:
                dp[i] += dp[i-c]

    print('num={0}, most: {1}'.format(num, dp[num]))




# 用指定的不限量的硬币凑指定的整数(最少的硬币数)
def ping_cou_coin(num):
    dp = [num+1]*(num+1)
    dp[0] = 0
    dp[1] = 1

    coins = [1, 2, 5, 10, 20, 50, 100]
    for k in range(len(coins)):
        for i in range(2, num+1):
            for j in range(k+1):
                if i-coins[j] > -1:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
    print('num={0}, least: {1}'.format(num, dp[num]))

num = int(sys.argv[1])
cou_coin_most(num)
ping_cou_coin(num)
