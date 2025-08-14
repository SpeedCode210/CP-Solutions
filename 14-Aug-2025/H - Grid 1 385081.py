# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

h,w = map(int,input().split())
grid = [input() for i in range(h)]

dp = [[0]*w for i in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            continue
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= 1000000007
print(dp[-1][-1])