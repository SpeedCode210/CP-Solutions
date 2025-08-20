# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    n = int(input())
    res = -1
    for i in range(33):
        if ((1 << i) ^ n) > 0 and ((1 << i) & n) > 0:
            res = 1 << i if res == -1 or 1 << i < res else res

    for i in range(33):
        for j in range(i):
            if (((1 << i) + (1 << j)) ^ n) > 0 and (((1 << i) + (1 << j)) & n) > 0:
                res = ((1 << i) + (1 << j)) if res == -1 or ((1 << i) + (1 << j)) < res else res
    print(res)
