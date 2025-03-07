# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())
for _ in range(t):
    m = int(input())
    p = [int(x) for x in input().split()]
    unit_size = 1
    res = 0
    while unit_size < m:
        for j in range(0,m, unit_size*2):
            if p[j+unit_size-1] > p[j+2*unit_size-1]:
                res += 1
                for i in range(unit_size):
                    p[j+i], p[j+unit_size+i] = p[j+unit_size+i], p[j+i]
                    
        unit_size *= 2
        
    for i in range(m-1):
        if p[i] > p[i+1]:
            res = -1
    print(res)