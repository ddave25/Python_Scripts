import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):

    common_elements = set(arr[0]).intersection(set(arr[1]))

    for i in range(2, len(arr)):
        common_elements = common_elements.intersection(set(arr[i]))

    return len(common_elements)


n = int(input())

arr = []

for _ in range(n):
    arr_item = input()
    arr.append(arr_item)

result = gemstones(arr)

print(result)
