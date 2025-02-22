# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

for i in range(5):
    k = [int(u) for u in input().split()]
    for j in range(5):
        if k[j] == 1:
            print(abs(i-2)+abs(j-2))