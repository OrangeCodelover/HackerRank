s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

a = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
b = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]

c = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
d = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

e = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
f = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

g = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
h = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

list = [a, b, c, d, e, f, g, h]
#list = a
#print(list)

cost = [0] * 8
#cost = 0
#print(cost)

for k in range(len(list)):
    for i in range (len(s)):
        for j in range(len(s[0])):
            cost[k] = cost[k] + abs(s[i][j]-list[k][i][j])
            print("subCost: ", cost[k])

print("cost:", min(cost))