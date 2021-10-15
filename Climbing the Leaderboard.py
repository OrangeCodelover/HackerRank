#ranked = [100, 90, 90, 80]
ranked = [100, 100,50,40,40,20,10]
player = [5, 25, 50,120]
scores = list(dict.fromkeys(ranked))
# player_ranked = [0]* len(player)
# print(player_ranked)
# ''' 
# # Works, need to be optimize
# for i in range(len(player)):
#     if player[i]< min(ranked):
#         player_ranked[i] = len(ranked)+1
#         # print(len(ranked)+1)
#     for j in range(len(ranked)):
#         #print("ranked score:",ranked[j])
#         #]=-089print("player score:", player[i])
#         if player[i] >= ranked[j]:
#             player_ranked[i] =  j+1
#             break
# print(player_ranked)



'''
for i in range(len(player)):
    ranked.append(player[i])
    ranked.sort(reverse=True)
    print("sorted rank:",ranked)
    player_ranked[i] = ranked.index(player[i]) + 1
    ranked.remove(player[i])

print(player_ranked)

'''
# scores = sorted(list(set(ranked)), reverse=True)
player_ranks = []
for score in player:
    while scores and score >= scores[-1]:
        scores.pop()
        print("scores:", scores)
    player_ranks.append(len(scores) + 1)

print(player_ranks)