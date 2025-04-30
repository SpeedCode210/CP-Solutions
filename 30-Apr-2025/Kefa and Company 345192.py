# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n,d = map(int,input().split())

A = []

for i in range(n):
    a,b = map(int,input().split())
    A.append((a,b))
    
A.sort()

maxi = A[0][1]
j = 0
total = A[0][1]

for i in range(n):
    if A[j][0] - A[i][0] < d:
        maxi = max(maxi, total)
        
        
    while A[j][0] - A[i][0] < d and j < n-1:
        j += 1
        total += A[j][1]
        if A[j][0] - A[i][0] < d:
            maxi = max(maxi, total)

            
    total -= A[i][1]
print(maxi)