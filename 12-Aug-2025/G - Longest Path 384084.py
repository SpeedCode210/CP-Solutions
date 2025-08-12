# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

n,m = map(int,input().split())

graph =[[] for i in range(n+1)]

dp = [-1]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
res = 0   
for i in range(1, n+1):
    if dp[i] > -1:
        res = max(res, dp[i])
        continue
    
    dfs = [i]
    
    while len(dfs):
        x = dfs[-1]
        if dp[x] == -1:
            dp[x] = -2
            for y in graph[x]:
                if dp[y] == -1:
                    dfs.append(y)
        else:
            dfs.pop()
            dp[x] = 0
            for y in graph[x]:
                dp[x] = max(dp[x], dp[y]+1)

    res = max(res, dp[i])
    
    
print(res)