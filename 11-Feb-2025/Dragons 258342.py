# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s,n = map(int, input().split())
 
S = []
 
for i in range(n):
    x,y = map(int, input().split())
    S.append(x*10001+y)
 
S.sort()
 
X = [u//10001 for u in S]
Y = [u%10001 for u in S]
 
result = "YES"
 
for i in range(len(X)):
    if s <= X[i]:
        result = "NO"
    else:
        s += Y[i]
print(result)