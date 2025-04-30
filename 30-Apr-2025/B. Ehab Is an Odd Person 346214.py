# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = input()
a = [int(x) for x in input().split()]

if len(a) == len([c for c in a if c%2 == 0]) or len([c for c in a if c%2 == 0]) == 0:
    print(*a)
else:
    print(*sorted(a))