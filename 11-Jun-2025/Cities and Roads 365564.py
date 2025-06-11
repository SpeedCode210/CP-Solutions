# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
res = 0
for i in range(n):
    res += sum([int(x) for x in input().split()])
print(res//2)