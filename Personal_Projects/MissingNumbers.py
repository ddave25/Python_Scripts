import math
import os
import random
import re
import sys

from collections import Counter

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):

    count_arr = Counter(arr)
    count_brr = Counter(brr)

    missing = []

    for k in count_brr.keys():
        if count_arr[k] !=  count_brr[k]:
            missing.append(k)

    return sorted(missing)

n = int(input())

arr = list(map(int, input().rstrip().split()))

m = int(input())

brr = list(map(int, input().rstrip().split()))

result = missingNumbers(arr, brr)

print(result)
