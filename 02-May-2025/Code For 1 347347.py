# Problem: Code For 1 - https://codeforces.com/problemset/problem/768/B


def f(n, l, r):

    if n == 0:
        return 0
    if n == 1:
        return 1 if l == r == 0 else 0
    
    m = n>>1
    
    nbD = m.bit_length()
    le = 2**nbD - 1
    res = 0
    
    
    if l < le:
        res += f(m, l, min(le-1, r))
        
    if r >= le and l <= le:
        res += n%2
        
    if r > le:
        res += f(m, max(l-le-1, 0), r-le-1)

    return res
    


N,L,R = map(int,input().split())
L -= 1
R -= 1
print(f(N, L, R))