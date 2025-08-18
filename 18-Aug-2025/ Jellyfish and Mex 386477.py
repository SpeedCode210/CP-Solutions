# Problem:  Jellyfish and Mex - https://codeforces.com/problemset/problem/1875/D

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    sup = [0]*(n+3)
    for x in a :
        if x < n+3:
            sup[x] += 1
            
    if sup[0] <= 1:
        print(0)
        continue
    
    dp = [1000000000]*(n+4)
    
    dp[-1] = 0
    res = 0
    for i in range(0, n+3):
        for j in range(0, i+1):
            dp[i] = min(dp[i], j + (i+1)*(sup[j]-1) + dp[j-1])
        if sup[i+1] == 0:
            res = dp[i]
            break
    print(res)