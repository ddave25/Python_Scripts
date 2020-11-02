import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    HourglassSum = 0
    maxHourglassSum = -64

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr)-2):
            HourglassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if HourglassSum > maxHourglassSum:
                maxHourglassSum = HourglassSum

    return maxHourglassSum


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

print(result)
