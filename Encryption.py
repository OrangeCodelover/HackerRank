#!/bin/python3

import math
import os
import random
import re
import sys


# Write your code here
s = 'feedthedo'
s_len = len(s)
print("S_len:",s_len)

root = math. sqrt(s_len)
if int(root + 0.5) ** 2 == s_len:
    row = int(root)
    col = int(root)
else:
    row = math.floor(root)
    col = row +1
    print("S_sqrt:", row )
    if row* col < s_len:
        row = col

print("row:", row )
print("col:", col )

i = 0 
string= ''
while i < s_len:
    string = string + s[i]
    if (i+1) % col:
        i = i + 1
    else:
        string = string + " "
        i = i + 1
print(string)

new_string= ''
for i in range(col):
    for j in range(row):
        if (i + col* j) > s_len-1:
            print("index_out:" ,i + col* j)
            break
        else:
            print("index :" ,i + col* j)
            new_string = new_string + s[i + j * col]
    new_string = new_string + " "

print("new string:",new_string)