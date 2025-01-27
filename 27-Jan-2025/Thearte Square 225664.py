# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

from math import ceil, floor
a = list(map(int, input().strip().split()))
print(ceil(a[0]/a[2])*ceil(a[1]/a[2]))
