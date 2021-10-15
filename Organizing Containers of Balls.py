import math
import os
import random
import re
import sys
#container = [[1,3,1],[2,1,2],[3,3,3]]
#container = [[0,2,1],[1,1,1],[2,0,0]]
container = [[2],[2],[1,1],[1,1],[2],[0,2],[1,1]]
#container = [[2],[3],[1,3,1],[2,1,2],[3,3,3],[3],[0,2,1],[1,1,1],[2,0,0]]

# Number of quaries
q = container[0][0]
container = container[1:]
array = [0]*q

# separate the 2D arrays
for i in range(q):
    array[i]= container[1:(1+container[0][0])]
    container = container[(1+container[0][0]) : ]
    print("array:",array)

for k in range(q):
    # Find the total number of each row
    row = len(array[k])
    col = len(array[k][0])

    #print("row:",row)
    #print("col:",col)
    col_m = [0] * col
    row_m = [0] * row

    # Find the total number of each row
    for i in range(row):
        row_m[i] = sum(array[k][i])

    #print("total in row:", sorted(row_m))

    # Find the total number of each col
    for i in range(col):
        for j in range(row):
            col_m[i] = col_m[i] + array[k][j][i]

    #print("total in col:", sorted(col_m))

    if sorted(col_m) == sorted(row_m):
        print("Possible")
    else: 
        print("Impossible")