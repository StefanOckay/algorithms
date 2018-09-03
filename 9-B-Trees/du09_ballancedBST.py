#!/usr/bin/env python3

# Povolene knihovny: copy, math
# Import jakekoli jine knihovny neprojde vyhodnocovaci sluzbou.
# To, ze jsou nejake knihovny povolene, neznamena, ze je nutne je pouzit.


# IB002 Domaci uloha 9.
#
# V teto uloze se budeme zabyvat binarnimi vyhledavacimi stromy.
#
# V prvni casti bude Vasi ulohou sestavit skoro uplny binarni vyhledavaci strom
# obsahujici zadane klice. Vstupni pole klicu bude usporadano od nejmensich po
# nejvetsi. Vas algoritmus musi mit LINEARNI casovou slozitost vzhledem k poctu
# zadanych klicu. Tento pozadavek je splnitelny diky usporadanosti pole na
# vstupu.
#
# V druhe casti bude Vasi ulohou zjistit, jestli zadany binarni vyhledavaci
# strom je skoro uplny. Pozadovana casova slozitost je linearni vuci poctu uzlu
# ve strome.
#
# Ve treti casti bude Vasi ulohou zjistit, jestli zadany binarni vyhledavaci
# strom ma vsechny listy ve stejne hloubce. Pozadovana casova slozitost je opet
# linearni vuci poctu uzlu ve strome.
#
# Skoro uplny strom ma zaplnena vsechna patra, jen posledni nemusi byt uplne
# zaplneno (a rovnez nemusi byt doleva zarovnane).
#
# Pro ilustraci, pro vstup (1,2,3,4,5,6,7,8,9,10) je korektnim vystupem
# algoritmu z prvni casti napriklad jeden z nasledujicich stromu:
#
#             ( 5 )                           ( 7 )
#            /     \                         /     \
#          (2)     (8)                  ( 4 )       ( 9 )
#         /  \     /  \                /     \      /   \
#       (1)  (3) (6)  (9)            (2)     (6)  (8)   (10)
#              \   \    \            / \     /
#              (4) (7)  (10)       (1) (3) (5)


# Do nasledujicich definic trid nijak nezasahujte.
# Pro vykreslovani stromu muzete pouzit dodanou funkci make_graph nize.

class BSTree:
    """Trida BSTree pro reprezentaci binarniho vyhledavacicho stromu.

    Atributy:
        root   koren stromu typu Node, nebo None, pokud je strom prazdny
    """

    def __init__(self):
        self.root = None


class Node:
    """Trida Node pro reprezentaci uzlu binarniho vyhledavaciho stromu.

    Atributy:
        data    hodnota daneho uzlu (zadana pri inicializaci)
        left    odkaz na leveho potomka typu Node, nebo None, pokud neexistuje
        right   odkaz na praveho potomka typu Node, nebo None, pokud neexistuje
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def build_sub_bst(last_node, array, low, high):
    """Vlozi novy uzel s klicem 'key' za node 'node', ktory nie je None."""
    # TODO
    if high < low:
        return
    mid = (low + high) // 2
    new_node = Node(array[mid])
    if last_node.data >= new_node.data and last_node.left is None:
        last_node.left = new_node
    else:
        last_node.right = new_node
    build_sub_bst(new_node, array, low, mid - 1)
    build_sub_bst(new_node, array, mid + 1, high)


# Ukol 1.
# Implementuje funkci build_bst, ktera dostane vzestupne serazeny seznam hodnot
# a vytvori z nich skoro uplny binarni vyhledavaci strom (typu BSTree).


def build_bst(array):
    """
    vstup: 'array' vzestupne serazene pole hodnot
    vystup: strom typu BSTree, ktery je skoro uplny (viz vyse) a obsahuje
            hodnoty z pole array
    casova slozitost: O(n), kde 'n' je delka array
    extrasekvencni prostorova slozitost:
         O(1), nepocitame do ni ovsem vstupni pole ani vystupni strom
    """
    # TODO
    lena = len(array)
    low = 0
    high = lena - 1
    mid = (low + high) // 2
    tree = BSTree()
    if lena > 0:
        tree.root = Node(array[mid])
        build_sub_bst(tree.root, array, low, mid - 1)
        build_sub_bst(tree.root, array, mid + 1, high)
    return tree


# Ukol 2.
# Implementujte funkci check_almost_complete, ktera dostane binarni vyhledavaci
# strom a otestujte, zda je skoro uplny.

def is_leaf(node):
    return node.right is None and node.left is None


def first_leaf_depth(node):
    if node is None:
        return -1
    if is_leaf(node):
        return 0
    if node.left is None:
        return first_leaf_depth(node.right) + 1
    return first_leaf_depth(node.left) + 1


def almost_same_depths(node, leafs_depth, current_depth):
    if is_leaf(node):
        return current_depth - leafs_depth < 2
    if node.left is not None:
        left_almost_same = almost_same_depths(node.left, leafs_depth, current_depth + 1)
    else:
        left_almost_same = True
    if node.right is not None:
        right_almost_same = almost_same_depths(node.right, leafs_depth, current_depth + 1)
    else:
        right_almost_same = True
    return left_almost_same and right_almost_same


def check_almost_complete(tree):
    """
    vstup: 'tree' binarni vyhledavaci strom typu BSTree
    vystup: True, pokud je 'tree' skoro uplny
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet uzlu stromu
    extrasekvencni prostorova slozitost: O(1) (nepocitame vstup)
    """
    # TODO
    if tree.root is None:
        return True
    if not is_leaf(tree.root.left) and tree.root.right is None:
        return False
    if not is_leaf(tree.root.right) and tree.root.left is None:
        return False
    leafs_depth = first_leaf_depth(tree.root)
    return almost_same_depths(tree.root, leafs_depth, 0)


# Ukol 3.
# Implementujte funkci check_all_leaves_same_depth, ktera overi, zda jsou
# vsechny listy zadaneho binarniho vyhledavaciho stromu ve stejne hloubce.

def same_depths(node, leafs_depth, current_depth):
    if is_leaf(node):
        return leafs_depth == current_depth
    if node.left is not None:
        left_same = same_depths(node.left, leafs_depth, current_depth + 1)
    else:
        left_same = True
    if node.right is not None:
        right_same = same_depths(node.right, leafs_depth, current_depth + 1)
    else:
        right_same = True
    return left_same and right_same



def check_all_leaves_same_depth(tree):
    """
    vstup: 'tree' binarni vyhledavaci strom typu BSTree
    vystup: True, pokud jsou vsechny listy 'tree' ve stejne hloubce
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet uzlu stromu
    extrasekvencni prostorova slozitost: O(1) (nepocitame vstup)
    """
    # TODO
    if tree.root is None:
        return True
    if tree.root.left is not None and tree.root.right is None:
        return False
    if tree.root.right is not None and tree.root.left is None:
        return False
    leafs_depth = first_leaf_depth(tree.root)
    return same_depths(tree.root, leafs_depth, 0)


# Pomocna funkce make_graph vygeneruje .dot soubor na zaklade stromu predaneho
# v argumentu. Cilem funkce je jen zobrazit aktualni stav daneho uzlu a jeho
# potomku, nijak nekontroluje jestli se jedna o BVS.
#
# Na vygenerovany soubor si bud najdete nastroj, nebo pouzijte odkazy:
# http://sandbox.kidstrythisathome.com/erdos/ nebo http://www.webgraphviz.com/
#
# Staci zkopirovat obsah souboru do formulare webove stranky.

def make_graph(tree, filename="bst.dot"):
    def dot_node(fd, node):
        if node is None:
            return

        fd.write('{} [label="{}"]\n'.format(id(node), node.data))

        for child, lr in (node.left, 'L'), (node.right, 'R'):
            dot_node(fd, child)
            dot_node_relations(fd, node, child, lr)

    def dot_node_relations(fd, parent, node, direction):
        if node is None:
            nil = direction + str(id(parent))
            fd.write('{} [label="",color=white]\n{} -> {}\n'
                     .format(nil, id(parent), nil))
        else:
            fd.write('{} -> {}\n'.format(id(parent), id(node)))

    with open(filename, "w") as fd:
        fd.write("digraph {\n")
        fd.write("node [color=lightblue2,style=filled]\n")
        dot_node(fd, tree.root)
        fd.write("}\n")

bst = build_bst([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9])
make_graph(bst)
print(check_almost_complete(bst))
print(check_all_leaves_same_depth(bst))