# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

# example below, replace it with your solution
n = int(input())
x = [[int(x) for x in input().split()] for i in range(n)]

sources = set(range(1, n+1))
sinks = set(range(1, n+1))

for i in range(n):
    for j in range(n):
        if x[i][j]:
            if j+1 in sources:
                sources.remove(j+1)
            if i+1 in sinks:
                sinks.remove(i+1)

a = sorted([x for x in sources])
print(len(a), *a)
a = sorted([x for x in sinks])
print(len(a), *a)