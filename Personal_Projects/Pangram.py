import math
import os
import random
import re
import sys
import string

# Complete the pangrams function below.
def pangrams(s):

    # convert to lower case, remove all spaces and punctuations
    s = s.lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))

    # remove repeat letters
    test = ''.join(sorted(set(s), key=s.index))

    if len(test) < 26:
        return "not pangram"
    else:
        return "pangram"


s = input()

result = pangrams(s)

print(result)
