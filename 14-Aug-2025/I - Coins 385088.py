# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

N = int(input())
p  = [float(x) for x in input().split()]

dp = [[0.0]*(N+1) for i in range(N+1)]

dp[0][0] = 1.0

def f (i,j):
    if i < 0 or j < 0:
        return 0.0
    return dp[i][j]

for i in range(1, N+1):
    for j in range(0, N+1):
        dp[i][j] = dp[i-1][j]*(1-p[i-1]) + dp[i-1][j-1]*(p[i-1])
        
print(sum(dp[N][(N+1)//2:]))