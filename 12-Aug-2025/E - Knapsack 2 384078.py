# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

n,W = map(int,input().split())

dp = [0] + [1000000001]*100001

for _ in range(n):
    w,v = map(int,input().split())
    for i in range(100000, v-1, -1):
        dp[i] = min(dp[i], w+dp[i-v])

        
for i in range(100000, -1, -1):
    if dp[i] <= W:
        print(i)
        break