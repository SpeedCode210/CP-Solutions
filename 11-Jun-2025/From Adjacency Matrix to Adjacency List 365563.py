# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())
for i in range(n):
    a = [int(x) for x in input().split()]
    print(len([x+1 for x in range(n) if a[x]]), *[x+1 for x in range(n) if a[x]])