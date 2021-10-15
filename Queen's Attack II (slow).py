n = 100
k= 100
r_q = 54
c_q = 30
obstacles =[[5,5], [4,1], [2,3],[5,2],[4,2]]

# Find all the positions
# store in pos
pos =[]
# Left
i = c_q -1
while i > 0:    
    pos.append([r_q,i])
    i -= 1

# Right
j = c_q + 1
while j < n+1:    
    pos.append([r_q,j])
    j += 1

# Up
k = r_q + 1
while k < n+1:
    pos.append([k,c_q])
    k += 1

# Down
l = r_q - 1
while l > 0:
    pos.append([l,c_q])
    l -= 1

# DownLeft
li= [r_q,c_q]
while li[0] > 1 and li[1] > 1 :
    pos.append([li[0]-1,li[1]-1]) 
    li[0] -= 1
    li[1] -= 1

# UpLeft
ki= [r_q,c_q]
while ki[0] < n and ki[1] > 1 :
    pos.append([ki[0]+1,ki[1]-1]) 
    ki[0] += 1
    ki[1] -= 1

# UpRight
kj= [r_q,c_q]
while kj[0] < n and kj[1] < n :
    pos.append([kj[0]+1,kj[1]+1]) 
    kj[0] += 1
    kj[1] += 1

# DownRight
lj= [4,3]
while lj[0] > 1 and lj[1] < n :
    pos.append([lj[0]-1,lj[1]+1]) 
    lj[0] -= 1
    lj[1] += 1


print("all_pos:",pos)
print("size:", len(pos))
# Remove the obstacles
if k == 0:
    print(len(pos))
for obstacle in obstacles:
    # If the obstacle is in the way
    if obstacle in pos:
        # Left
        if obstacle[1] < c_q and obstacle[0] == r_q:
            for left in range(obstacle[1]):
                if [r_q,left+1] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([r_q,left+1])
        
        # Right
        if obstacle[1] > c_q and obstacle[0] == r_q:
            for right in range(n + 1 - obstacle[1]):
                if [r_q,c_q + 1 + right] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([r_q,c_q + 1 + right])

        # Up
        if obstacle[0] > r_q and obstacle[1] == c_q:
            for up in range(n + 1 - obstacle[0]):
                if [r_q + 1 + up,c_q] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([r_q + 1 + up,c_q])
        # Down
        if obstacle[0] < r_q and obstacle[1] == c_q:
            for down in range(obstacle[0]):
                if [down+1,c_q] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([down+1,c_q])

        # LeftUp
        if obstacle[0] > r_q and obstacle[1] < c_q:
            for leftup in range(min(obstacle[1],n + 1 - obstacle[0])):
                if [obstacle[0]+leftup,obstacle[1]-leftup] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([obstacle[0]+leftup,obstacle[1]-leftup])
        
        # LeftDown
        if obstacle[0] < r_q and obstacle[1] < c_q:
            for leftdown in range(min(obstacle[1],obstacle[0])):
                if [obstacle[0]-leftdown,obstacle[1]-leftdown] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([obstacle[0]-leftdown,obstacle[1]-leftdown])

        # RightDown
        if obstacle[0] < r_q and obstacle[1] > c_q:
            for rightdown in range(min(obstacle[1],obstacle[0])):
                if [obstacle[0]-rightdown,obstacle[1]+ rightdown] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([obstacle[0]-rightdown,obstacle[1]+ rightdown])

        # RightUp
        if obstacle[0] > r_q and obstacle[1] > c_q:
            for rightup in range(min(obstacle[1],obstacle[0])):
                if [obstacle[0]+ rightup,obstacle[1]+ rightup] not in pos:
                    pos.remove(obstacle)
                    break
                else:
                    pos.remove([obstacle[0]+ rightup,obstacle[1]+ rightup])

        

        
print("pos:",pos)
print("size:", len(pos))