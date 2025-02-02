# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

S = "codeforces"
t = int(input())
for i in range(t):
    s = input()
    x = 0
    for j in range(10):
        if S[j] != s[j]: 
            x += 1
    print(x)