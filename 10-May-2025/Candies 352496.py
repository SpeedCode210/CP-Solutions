# Problem: Candies - https://codeforces.com/contest/1810/problem/B

t = int(input())
for i in range(t):
    n = int(input())
    res = []
    ans = True
    while n > 1:
        if n%4 == 3:
            n = (n-1)//2
            res.append(2)
        elif n%4 == 1:
            n = (n+1)//2
            res.append(1)
        else:
            ans = False
            break
    if ans:
        print(len(res))
        print(*reversed(res))
    else:
        print(-1)
        