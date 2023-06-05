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
#         # sépare la liste en deux et arrondi a l'entier avec le math.floor 
#         # (ex : longueur de liste = 7)
#         # longueur de liste 1 = 3 et liste 2 = 4
#         part1 = list[0:math.floor(len(list)/2)]
#         part2 = list[math.floor(len(list)/2):len(list)]

#         part1Tri = tri_fusion(part1)
#         part2Tri = tri_fusion(part2)
#         newList = []

#         for i in range(len(list)):
#             if len(part1Tri) == 0:
#                 newList.append(part2Tri[0])
#                 part2Tri.remove(part2Tri[0])
#                 # newList.append(part2Tri.pop())
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

# print(tri_fusion(tab))


# ============================================================================
# TRI PAR INSERTION
# ============================================================================
# def tri_insertion(list):
#     for i in range(1, len(tab)): 
#         actual = tab[i] 
#         j = i-1

#         while j >= 0 and actual < tab[j] : 
#             tab[j + 1] = tab[j] 
#             j -= 1
#         tab[j + 1] = actual

# print(tri_insertion(tab))




# for i in range(1, len(tab)) :
#     actualNbr = tab[i]
    
#     # décalage des éléments du tableau }
#     while i > 0 and tab[i-1] > actualNbr :
#         tab[i] = tab[i-1]
#         i -= 1
        
#     # insère l'élément à sa place
#     tab[i] = actualNbr

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


# permutation, sens, i = True, 1, 0
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






# ============================================================================
# TRI RAPIDE (correction)
# ============================================================================ 

# def quicksort(liste:list) -> list:
#     if len(liste) <= 1:
#         return liste
    
#     pivot_index = len(liste) - 1
#     pivot = liste[pivot_index]
    
#     liste_gauche = [elt for elt in liste[:pivot_index] if elt <= pivot]
#     liste_droite = [elt for elt in liste[:pivot_index] if elt > pivot]
    
#     return quicksort(liste_gauche) + [pivot] + quicksort(liste_droite) 

# print(quicksort([0, 0, 1, 15, 20, -4, 2, 1, 7, 18, 7]))



# ============================================================================
# TRI PAR TAS
# ============================================================================ 




# ============================================================================
# TRI PAR SELECTION 
# ============================================================================ 

