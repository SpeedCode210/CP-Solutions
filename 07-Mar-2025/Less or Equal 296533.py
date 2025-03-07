# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n,k = map(int,input().split())
x = [int(x) for x in input().split()]

x.sort()

if k == 0:
    if x[0] == 1:
        print("-1")
    else:
        print(1)
else:
    if k == n:
        print(1000000000)
    else:
        if x[k] != x[k-1]:
            print(x[k]-1)
        else:
            print(-1)