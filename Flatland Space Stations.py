n = 90
c = [76,16,71,56,77,31,66,32,57,19,14,42]

# order the space station
c.sort()
print(c)

end_gap = n-1 - c[-1]
start_gap = c[0]
print("end_gap: ", end_gap)
print("start_gap: ", start_gap)

m = len(c)
# find the biggest gap in the list 
gap = 0
for i in range(m-1):
    if c[i+1] - c[i] > gap:
        gap = c[i+1] - c[i]
print("end_gap: ", end_gap)
print("gap:", gap)
# the last gap
if end_gap > (gap//2) and end_gap >= start_gap:
    print("end_gap:", end_gap)
# the first gap
elif start_gap > (gap//2) and end_gap <= start_gap:
    print("start_gap:", start_gap)
# gap is even number
elif gap % 2 == 0:
    print("even:", int(gap/2))
# gap is odd number
else:
    print("odd:",gap//2)
