import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    factorial = 1
    for i in range(n):
        factorial = factorial * (n-i)
    
    print("Factorial is : ", factorial)

if __name__ == '__main__':
    extraLongFactorials(3)
