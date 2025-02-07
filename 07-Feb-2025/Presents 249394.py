# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
arr = [0]*n
inp = [int(k) for k in input().split()]
for i in range(n):
    arr[inp[i]-1] = i+1

print(" ".join([str(k) for k in arr]))