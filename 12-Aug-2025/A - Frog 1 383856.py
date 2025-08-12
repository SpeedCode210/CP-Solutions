# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = [int(x) for x in input().split()] + [1000000000]

dp = [0]*n + [1000000000]

for i in range(n-2, -1,-1):
    dp[i] = min(dp[i+1] + abs(h[i+1]-h[i]), dp[i+2] + abs(h[i+2]-h[i]))
print(dp[0])