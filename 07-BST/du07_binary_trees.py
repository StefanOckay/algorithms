#!/usr/bin/env python3

# Povolene knihovny: copy, math
# Import jakekoli jine knihovny neprojde vyhodnocovaci sluzbou.
# To, ze jsou nejake knihovny povolene, neznamena, ze je nutne je pouzit.


# IB002 Domaci uloha 7.
#
# Souctovy strom je binarni strom, kde kazdy uzel ma nasledujici vlastnost:
# Pokud ma uzel alespon jednoho syna, potom je klic uzlu roven souctu klicu
# vsech jeho synu. Listy stromu tedy mohou obsahovat libovolne hodnoty.
# Za souctovy je povazovan i strom, ktery neobsahuje zadne uzly, a strom,
# ktery obsahuje prave jeden uzel.
#
# Muzete si samozrejme pridat vlastni pomocne funkce.
#
# Priklad:
# souctove stromy      nesouctove stromy
#   53       47            53       47
#  /  \        \          /  \     /
# 21  32       47        21  21   46
#             /  \                  \
#            1    46                 1

# Do nasledujicich definic trid nijak nezasahujte.
#
# Trida pro reprezentaci souctoveho stromu.
# root je koren stromu a je typu Node, nebo None, pokud je strom prazdny.
#
# Pro vykreslovani stromu muzete pouzit funkci make_graph z cv07.

class SumTree:
    def __init__(self):
        self.root = None


# Trida pro reprezentaci uzlu v souctovem strome.
# key je hodnota uzlu, ktera ma byt rovna souctu hodnot vsech synu.

class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


# Ukol 1.
# Vasim prvnim ukolem je napsat funkci, ktera vybuduje uplny souctovy strom ze
# zadaneho pole. Listy stromu budou prave prvky pole v poradi zleva doprava.
# Delka pole bude vzdy mocninou dvojky.
#
# Napriklad:
# Z pole [1,2,3,4] vznikne strom:
#      10
#    /    \
#   3      7
#  / \    / \
# 1   2  3   4


def left_index(index):
    return 2 * index + 2


def right_index(index):
    return 2 * index + 1


def tree_root(array, index, lena):
    if index >= lena:
        return None
    node = Node()
    node.key = array[index]
    node.right = tree_root(array, right_index(index), lena)
    node.left = tree_root(array, left_index(index), lena)
    return node


def build_sum_tree(array):
    """
    vstup: pole (Pythonovsky seznam) 'array' cisel delky 'n',
           kde 'n' je nejaka mocnina dvojky
    vystup: korektni strom typu SumTree, ktery ma v listech (v poradi zleva
            doprava) hodnoty ze zadaneho pole 'array'
            strom musi byt uplny, tj. vsechna jeho patra musi byt zcela
            zaplnena
    casova slozitost: O(n)
    """
    # TODO
    lena = len(array)
    tree_array = []
    len_tree_array = 2 * lena - 1
    half = (len_tree_array + 1) // 2
    for i in range(0, half):
        tree_array.append(array[i])
    i = 0
    while i < len_tree_array - 1:
        app = tree_array[i] + tree_array[i + 1]
        tree_array.append(app)
        i += 2
    downto_array = list(reversed(tree_array))
    tree = SumTree()
    tree.root = tree_root(downto_array, 0, len_tree_array)
    return tree


# Ukol 2.
# Vasim druhym ukolem je napsat funkci is_sum_tree, ktera overi, zda je strom
# souctovy. Pokud ano, vraci True, jinak False.


def is_sum_subtree(node):
    if node is None or (node.right is None and node.left is None):
        return True
    if node.right is None:
        right_key = 0
    else:
        right_key = node.right.key
    if node.left is None:
        left_key = 0
    else:
        left_key = node.left.key
    if left_key + right_key != node.key:
        return False
    return is_sum_subtree(node.left) and is_sum_subtree(node.right)


def is_sum_tree(tree):
    """
    vstup: 'tree' typu SumTree
           (je zaruceno, ze uzly ve strome jsou typu Node;
            neni zaruceno, ze splnuji souctovou podminku)
    vystup: True, pokud je 'tree' korektni SumTree, tj. vsechny jeho uzly
                  splnuji souctovou podminku
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet prvku 'tree'
    """
    # TODO
    return is_sum_subtree(tree.root)