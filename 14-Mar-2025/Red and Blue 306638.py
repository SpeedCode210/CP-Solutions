# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    maxa = 0
    maxb = 0
    suma = 0
    sumb = 0
    for c in a:
        suma += c
        maxa = max(maxa, suma)
    for c in b:
        sumb += c
        maxb = max(maxb, sumb)
    print(maxa+maxb)