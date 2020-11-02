#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    letterOccurs = s.count('a')

    remainingLetters = n - (len(s) * math.floor(n/len(s)))

    return (letterOccurs*math.floor(n/len(s))) + s[0:remainingLetters].count('a')


s = input()

n = int(input())

result = repeatedString(s, n)

print(str(result) + '\n')
