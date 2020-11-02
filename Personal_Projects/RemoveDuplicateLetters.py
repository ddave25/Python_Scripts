import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    prev = '\0'
    LetterFirstAppearance = 0

    for i in range(len(s)):

        if prev != s[i]:
            LetterFirstAppearance += 1
            prev = s[i]

    return len(s) - LetterFirstAppearance


q = int(input())

for q_itr in range(q):
    s = input()

    result = alternatingCharacters(s)

    print(result)
