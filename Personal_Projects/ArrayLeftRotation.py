#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    temp = []

    temp.extend(a[d:])
    temp.extend(a[0:d])

    return temp


nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)

print(' '.join(map(str, result)))
print('\n')

