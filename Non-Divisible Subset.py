k = 3
s = [1,7,2,4]
# k = 4
# s = [19,10,12,10,24,25,22]
reminder = [0]*k
max_sub = 0
for i in s:
    reminder[i%k] += 1


print("reminder", reminder)
# first element
max_sub = max_sub + min(reminder[0], 1)
print("max subset:", max_sub)

# k is even number
if k % 2 == 0:
    for i in range(k//2-1):
        max_sub = max_sub + max(reminder[i+1],reminder[k-i-1])
    # for the mid
    max_sub = max_sub + min (reminder[k//2],1)
    #print("i:", i)
# k is odd number
elif k % 2:
    for i in range(k//2):
        max_sub = max_sub + max(reminder[i+1],reminder[k-i-1])


print("max subset_2:", max_sub)