# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    N = [int(x) for x in input().split()]
    M = sorted([int(x) for x in input().split()])
    
    ans = True
    p = 0
    N[0] = min(N[0], M[0] - N[0])
    for i in range(1,n):
        a = 0
        b = len(M) - 1
        while a < b:
            middle = (a+b+1)//2
            if M[middle-1] - N[i] >= N[i-1]:
                b = middle-1
            else:
                a = middle
        
        if M[a] - N[i] >= N[i-1] and not(N[i] >= N[i-1]):
            N[i] = M[a] - N[i]
        elif not(M[a] - N[i] >= N[i-1]) and (N[i] >= N[i-1]):
            N[i] = N[i]
        elif (M[a] - N[i] >= N[i-1]) and (N[i] >= N[i-1]):
            N[i] = min((M[a] - N[i]), (N[i]))
        else: 
            ans = False
            break
    
    print("YES" if ans else "NO")