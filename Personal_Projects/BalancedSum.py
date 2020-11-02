import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):

    right_sum = 0
    left_sum = 0

    result = "NO"

    for i in range(len(arr)):
        right_sum += arr[i]

    for i in range(len(arr)):

        right_sum -= arr[i]

        if left_sum == right_sum:
            result = "YES"
            break

        left_sum += arr[i]

    return result


T = int(input().strip())

for T_itr in range(T):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = balancedSums(arr)

    print(result + '\n')