n = 100
k= 100
r_q = 54
c_q = 30
obstacles =[[48, 36], [38, 46], [60, 24], [70, 14], [54, 36], [54, 24], [60, 30], [48, 30], [71, 50], [14, 97], [47, 31], [29, 68], [90, 10], [36, 85], [63, 24], [32, 13], [64, 57], [45, 57], [86, 19], [43, 86], [68, 72], [29, 25], [48, 59], [38, 78], [45, 16], [40, 92], [76, 85], [40, 10], [65, 16], [71, 18], [90, 40], [65, 45], [10, 37], 
[19, 82], [42, 56], [46, 60], [94, 14], [34, 36], [95, 49], [78, 67], [86, 23], [28, 12], [95, 57], [38, 19], [61, 49], [67, 42], [28, 25], [38, 28], [91, 20], [90, 86], [81, 19], [18, 43], [29, 69], [36, 20], [72, 75], [39, 50], [17, 92], [48, 25], [20, 79], [82, 57], [58, 50], [94, 70], [17, 19], [73, 20], [45, 12], [19, 89], [45, 12], [59, 74], [63, 71], [32, 23], [67, 85], [24, 25], [18, 61], [97, 50], [70, 37], [30, 10], [39, 90], [75, 58], [58, 34], [47, 62], [28, 28], [79, 34], [73, 80], [93, 36], [25, 45], [48, 75], [42, 13], [18, 69], [35, 21], [18, 87], [57, 19], 
[26, 92], [94, 34], [84, 48], [61, 95], [62, 89], [59, 74], [50, 40], [36, 37], [95, 62]]

# all possible locations
left = c_q - 1
right = n - c_q
print("beginner",right)
up = n - r_q
down = r_q - 1

upleft = min(up,left)
upright = min(up,right)
downleft = min(down, left)
downright = min(down, right)

#obstacles
for obstacle in obstacles:
    # left
    if obstacle[0] == r_q and obstacle[1] < c_q:
        if c_q- 1-obstacle[1] < left:
            left = c_q -1 -obstacle[1]

    # right
    elif obstacle[0] == r_q and obstacle[1] > c_q:
        if obstacle[1]- c_q -1 < right:
            right = obstacle[1]- c_q-1
    # up
    elif obstacle[0] > r_q and obstacle[1] == c_q:
        if obstacle[0]-r_q -1 < up:
            up = obstacle[0]-r_q -1

    # down
    elif obstacle[0] < r_q and obstacle[1] == c_q:
        if r_q- 1-obstacle[0] < down:
            down = r_q- obstacle[0]-1

    # upleft
    elif obstacle[0] > r_q and obstacle[1] < c_q:
        if obstacle[0] - r_q == c_q - obstacle[1]:
            if obstacle[0]- r_q - 1< upleft:
                upleft = obstacle[0]- r_q - 1

    # upright
    elif obstacle[0] > r_q and obstacle[1] > c_q:
        if obstacle[0] - r_q == obstacle[1] - c_q:
            if obstacle[0]- r_q - 1< upright:
                upright = obstacle[0]- r_q - 1

    # downleft
    elif obstacle[0] < r_q and obstacle[1] < c_q:
        if r_q - obstacle[0]  == c_q - obstacle[1]:
            if r_q - obstacle[0] - 1< downleft:
                downleft = r_q -obstacle[0] - 1

    # downright
    elif obstacle[0] < r_q and obstacle[1] > c_q:
        if r_q - obstacle[0]  == obstacle[1]-c_q:
            if r_q - obstacle[0] - 1< downright:
                downright = r_q -obstacle[0] - 1
attack = left + right + up + down + downleft + downright + upleft + upright
print("left",left)
print("right",right)
print("up", up)
print("down", down)
print("upleft", upleft)
print("upright", upright)
print("downleft", downleft)
print("downright", downright)
print("total:",attack)

      
