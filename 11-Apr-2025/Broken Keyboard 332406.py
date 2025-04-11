# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

t= int(input())
for _ in range(t):
    s = input()
    s= s + "$"
    last = " "
    count = 2
    S = set()
    for i in range(len(s)):
        if s[i] == last:
            count += 1
        else:
            if count%2 == 1:
                S.add(last)
            count = 1
            last = s[i]
        if s[i] == '$':
            break
    print("".join(sorted([x for x in S])))