import math
import os
import random
import re
import sys



arr = [1,2,3,4,5]
max = max(arr)
min = min(arr)

minsum = sum(arr) - max
maxsum = sum(arr) - min

print (minsum, maxsum )