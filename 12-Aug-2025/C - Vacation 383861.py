# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
dp = [0,0,0]
for i in range(n):
    a,b,c = map(int,input().split())
    dp = [max(dp[1], dp[2])+a, b+max(dp[0], dp[2]), c+max(dp[0], dp[1])]
print(max(dp))