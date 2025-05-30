# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

def gcd(a,b):
    if a > b:
        a,b = b,a
    if a == 0:
        return b
    return gcd(a,b%a)

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    if(sum(a) == 0):
        print(*[i for i in range(1, n+1)])
        continue
    u = 0
    for j in range(32):
        u = gcd(u, len([x for x in a if (x//(2**j))%2]))
    
    print(*[i for i in range(1, n+1) if u%i == 0])