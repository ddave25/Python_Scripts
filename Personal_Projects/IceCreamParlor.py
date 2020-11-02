import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):

    firstChoicePricePosition = 0
    secondChoicePricePosition = len(arr)

    i = len(arr) - 1

    while i != firstChoicePricePosition:

        if arr[i] == (m - arr[firstChoicePricePosition]):
            secondChoicePricePosition = i
            break

        else:
            if i == firstChoicePricePosition + 1:
                firstChoicePricePosition += 1
                i = len(arr) - 1
            else:
                i -= 1

    return sorted([firstChoicePricePosition+1, secondChoicePricePosition+1])


t = int(input())

for t_itr in range(t):

    m = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = icecreamParlor(m, arr)

    print(result)

    print('\n')
