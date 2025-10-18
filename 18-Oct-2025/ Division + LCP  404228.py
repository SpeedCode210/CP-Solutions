# Problem:  Division + LCP  - https://codeforces.com/contest/1968/problem/G1

t = int(input())
for _ in range(t):
    n,l,r = map(int,input().split())
    s = input()   
    
    a = 0
    b = n
    
    while a < b:
        m = (a+b+1)//2
        c = 1
        p = 0
        i = 1
        
        pref1 = [0]*m
        
        while i < m:
            if s[i] == s[p]:
                p += 1
                pref1[i] = p
                i += 1
            elif p > 0:
                p = pref1[p-1]
            else:
                i += 1
                
        p = 0
        while i < n:
            if s[i] == s[p]:
                p += 1
                if p == m:
                    c += 1
                p %= m
                i += 1
            elif p > 0:
                p = pref1[p-1]
            else:
                i += 1
        
        
        if c >= l:
            a = m
        else:
            b = m-1
            
    print(a)
