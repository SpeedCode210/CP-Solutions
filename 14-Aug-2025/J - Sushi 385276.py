# Problem: J - Sushi - https://atcoder.jp/contests/dp/tasks/dp_j

n = int(input())
A = [int(x) for x in input().split()]
dp  = [-1 for i in range(4590551)]
u = -1

blocks = [[0]*(300+1) for i in range(301)]
for i in range(300+1):
    for j in range(300+1-i):
        blocks[i][j] = u+1
        for k in range(300+1-i-j):
            u += 1
            
dp[blocks[n][0]] = (0.0,0.0)
dp[blocks[A.count(3)][A.count(2)] + A.count(1)] = (1.0,0.0)

def f(a, b, c, d):
    return dp[blocks[a][b] + c]

dfs = [(0,0,0,n)]
while len(dfs):
    x = dfs[-1]
    a,b,c,d = x
    p = 0.0
    E = 0.0
    if b :
        if f(a+1, b-1, c, d) == -1:
            dfs.append((a+1, b-1, c, d))
            continue
        p += f(a+1, b-1, c, d)[0]*((a+1)/n)*(n/(n-d))
        E += (f(a+1, b-1, c, d)[1] + (n/(n-d)))*f(a+1, b-1, c, d)[0]*((a+1)/n)*(n/(n-d))
    if c :
        if f(a, b+1, c-1, d) == -1:
            dfs.append((a, b+1, c-1, d))
            continue
        p += f(a, b+1, c-1, d)[0]*((b+1)/n)*(n/(n-d))
        E += (f(a, b+1, c-1, d)[1] + (n/(n-d)))*f(a, b+1, c-1, d)[0]*((b+1)/n)*(n/(n-d))
    if d :
        if f(a, b, c+1, d-1) == -1:
            dfs.append((a, b, c+1, d-1))
            continue
        p += f(a, b, c+1, d-1)[0]*((c+1)/n)*(n/(n-d+1))
        E += (f(a, b, c+1, d-1)[1] + (n/(n-d+1)))*f(a, b, c+1, d-1)[0]*((c+1)/n)*(n/(n-d+1))
    
    dp[blocks[a][b] + c] = (p,E/p if p != 0 else 0)
    
    dfs.pop()


print(dp[blocks[0][0] + 0][1])