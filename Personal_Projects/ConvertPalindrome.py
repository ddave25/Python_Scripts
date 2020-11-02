import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):

    ops = 0

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            ops += max(ord(s[i]), ord(s[j])) - min(ord(s[i]), ord(s[j]))

        i += 1
        j -= 1

    return ops


q = int(input())

for q_itr in range(q):
    s = input()

    result = theLoveLetterMystery(s)

    print(result)

