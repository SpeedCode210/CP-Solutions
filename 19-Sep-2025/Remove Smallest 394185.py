# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print("NO")
            break
    else:
        print("YES") 