# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

t = int(input())
D = dict()
for i in range(t):
    D[input()] = i
print("\n".join([x[1] for x in sorted([(-D[i],i) for i in D])]))