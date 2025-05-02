# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def p(n : int):
    if n > 1:
        p(n-1)
    print(n, end=' ')

n = int(input())
p(n)