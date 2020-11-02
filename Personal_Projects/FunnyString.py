import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):

    reverseS = ''.join(reversed(s))

    s_diff = []
    reverseS_diff = []

    for i in range(len(s)-1):
        s_diff.append(abs(ord(s[i]) - ord(s[i+1])))

    for i in range(len(reverseS)-1):
        reverseS_diff.append(abs(ord(reverseS[i]) - ord(reverseS[i+1])))

    if s_diff != reverseS_diff:
        return "Not Funny"
    else:
        return "Funny"


q = int(input())

for q_itr in range(q):
    s = input()

    result = funnyString(s)

    print(result)
