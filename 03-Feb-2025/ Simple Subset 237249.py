# Problem:  Simple Subset - https://codeforces.com/contest/665/problem/D

# Note : This gets TLE if not using PyPy
k = dict([(0,0)])
eratosthenes = [True] * 2000002
for i in range(2,2000002):
    if not(eratosthenes[i]):
        continue
    m = 2*i
    while m < 2000002:
        eratosthenes[m] = False
        m += i

n = int(input())
pair = []
ones = 0

for u in [int(y) for y in input().split()]:
    for key in k.keys():
        if key == 0:
            continue
        if key != 0 and eratosthenes[u+key]:
            pair = [key, u]
    k[u] = 1
    if u == 1:
        ones += 1

if ones > 1:
    pair = [1]*ones
    for key in k.keys():
        if key < 2:
            continue
        if eratosthenes[key+1]:
            pair.append(key)
            break

if len(pair) ==0:
    for key in k.keys():
        if key > 0:
            pair = [key]
            break

print(len(pair))
print(" ".join([str(y) for y in pair]))