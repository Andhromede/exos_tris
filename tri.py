import random
import math


tab = []
for i in range(50):
    tab.append(random.randrange(800))


# ============================================================================
## TRI PAR FUSION
# ============================================================================

# def tri_fusion(list):
#     if len(list) > 1:
#         part1 = list[0:math.floor(len(list)/2)]
#         part2 = list[math.floor(len(list)/2):len(list)]

#         part1Tri = tri_fusion(part1)
#         part2Tri = tri_fusion(part2)

#         newList = []

#         for i in range(len(list)):
#             if len(part1Tri) == 0:
#                 newList.append(part2Tri[0])
#                 part2Tri.remove(part2Tri[0])
#             elif len(part2Tri) == 0:
#                 newList.append(part1Tri[0])
#                 part1Tri.remove(part1Tri[0])
#             elif part1Tri[0] < part2Tri[0]:
#                 newList.append(part1Tri[0])
#                 part1Tri.remove(part1Tri[0])
#             else:
#                 newList.append(part2Tri[0])
#                 part2Tri.remove(part2Tri[0])
#         list = newList
#     return list

# print(tab)
# print(tri_fusion(tab))


# ============================================================================
# TRI PAR INSERTION
# ============================================================================
# for i in range(1, len(tab)): 
#     k = tab[i] 
#     j = i-1
#     while j >= 0 and k < tab[j] : 
#         tab[j + 1] = tab[j] 
#         j -= 1
#     tab[j + 1] = k

# print(tab)


# ============================================================================
# TRI A BULLES
# ============================================================================ 

# permutation = True
# passage = 0

# while permutation == True:
#     permutation = False
#     passage += 1

#     for i in range(0, len(tab) - passage):
#         if tab[i] > tab[i + 1]:
#             permutation = True
#             tab[i], tab[i + 1] = \
#             tab[i + 1],tab[i]

# print(tab)


# ============================================================================
# TRI COCKTAIL 
# ============================================================================ 



# ============================================================================
# TRI A PEIGNE 
# ============================================================================ 

