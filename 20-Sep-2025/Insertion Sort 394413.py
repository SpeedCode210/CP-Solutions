# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] > x:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = x
            print(*arr)
            break
    else:
        arr[0] = x
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
