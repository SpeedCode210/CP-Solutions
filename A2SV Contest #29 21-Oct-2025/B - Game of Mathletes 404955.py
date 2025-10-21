# Problem: B - Game of Mathletes - https://codeforces.com/gym/633600/problem/B

from collections import Counter
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = [0]*(2*n+2)
    b = [int(x) for x in input().split()]
    for x in b:
        a[x] += 1
    score = 0
    for i in range(2*n+2):
        if i*2 == k:
            score += a[i] - a[i]%2
        else:
            if i <= k:
                score += min(a[i], a[k-i])
    print(score//2)
