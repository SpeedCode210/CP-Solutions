# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def f(n):
    if n == 0:
        return 1
    
    # calculate the sum each time
    # and return final answer
    return 1 + f(n-1)/3

n = input()

print(f(n))