# Problem: A - Zhan's Blender - https://codeforces.com/gym/633600/problem/A

t = int(input())
 
for _ in range(t):
    n = int(input())
    x,y = map(int,input().split())
    x = min(x,y)
    print((n+x-1)//x)
