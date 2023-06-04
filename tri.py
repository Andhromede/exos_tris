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
# """
# le tri a bulle compare 2 chiffres qui se suivent et les inversent si nécéssaire. 
# Arrivé a la fin du tableau, il recommance depuis le début et ceux jusqu'au tri 
# complet de tout le tableau.

# switch = le flag qui permet de mettre fin a la boucle
# nbTurn = permet d'exclure le(s) dernier(s) chiffre(s) du tableau (deja trié(s)) a chaque tour
# """

# switch = True
# nbTurn = 0

# while switch == True:
#     nbTurn += 1
#     switch = False

#     for i in range(0, len(tab) - nbTurn):
#         if tab[i+1] < tab[i]:
#             switch = True
#             tab[i], tab[i + 1] = tab[i + 1], tab[i]

# print(tab)


# ============================================================================
# TRI COCKTAIL 
# ============================================================================ 
# """
# le tri cocktail fonctionne comme le tri à bulle sauf qu'il vas vers l'avant puis vers l'arrière
# switch = le flag qui permet de stopper la boucle
# sens = pour permettre au "curseur" d'aller en avant puis en arrière
# i = "curseur"
# debut = index de départ du tableau
# fin = longueur du tableau -2 afin de ne pas essayer de comparer le dernier chiffre avec le suivant (qui n'éxiste pas)
# """


## permutation, sens, i = True, 1, 0
# switch = True 
# sens = 1
# i = 0
# debut = 0
# fin = len(tab)-2

# while switch == True:
#     switch = False
#     while (i < fin and sens == 1) or (i > debut and sens == -1) :
#         # Si le chiffre actuelle est > au suivant ...
#         if tab[i] > tab[i + 1]:
#             switch = True
#             # echange les deux elements
#             tab[i], tab[i + 1] = tab[i + 1], tab[i]
#         # fait avancer le "curseur" vers l'avant ou vers l'arrière
#         i = i + sens
    
#     # On change le sens du parcours
#     if sens == 1:
#         fin = fin - 1
#     else:
#         debut = debut + 1
#     sens = -sens

# print(tab)

# ============================================================================
# TRI A PEIGNE 
# ============================================================================ 

