import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):

    lastEntry = arr[n-1]

    for i in range(n-1, -1, -1):

        if i == 0 and arr[i] > lastEntry:

            arr[i] = lastEntry

            print(" ".join(str(i) for i in arr[::1]))

        elif arr[i-1] > lastEntry:

            arr[i] = arr[i - 1]

            print(" ".join(str(i) for i in arr[::1]))

        else:

            arr[i] = lastEntry

            print(" ".join(str(i) for i in arr[::1]))

            break


n = int(input())

arr = list(map(int, input().rstrip().split()))

insertionSort1(n, arr)
