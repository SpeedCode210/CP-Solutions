# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

n, k= map(int,input().split())
h = [int(x) for x in input().split()]

dp = [0]*n

for i in range(n-2, -1,-1):
    dp[i] = min([dp[x] + abs(h[x]-h[i]) for x in range(i+1, min(i+k+1, n))])
print(dp[0])