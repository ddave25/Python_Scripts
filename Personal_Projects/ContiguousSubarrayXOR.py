import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr):

    if len(arr) % 2 == 0:
        return 0
    else:
        XORValue = 0

        for i in range(0, len(arr), 2):
            XORValue = XORValue ^ arr[i]

        return XORValue


t = int(input())

for t_itr in range(t):
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = sansaXor(arr)

    print(str(result) + '\n')
