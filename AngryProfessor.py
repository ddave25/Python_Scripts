import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):

    a.sort()

    count = 0

    for i in range(k+1):

        if a[i] <= 0:
            count+=1
        else:
            break

    if count < k:
        return "YES"
    else:
        return "NO"


t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)

    print(result, '\n')

