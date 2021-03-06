#!/usr/bin/env python3
import math
from enum import Enum


# definice barev
class Colors(Enum):
    red = 1
    black = 2


class Node:
    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu
        color   muze nabyvat hodnoty 'red' a 'black'
        parent  reference na rodice uzlu
        left    reference na leveho potomka
        right   reference na praveho potomka
    """

    def __init__(self):
        self.key = 0
        self.color = Colors.black
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    """Trida RedBlackTree slouzi k reprezentaci cerveno-cerneho
    vyhledavaciho stromu.

    Atributy:
        root    reference na korenovy uzel typu Node
    """

    def __init__(self):
        self.root = None


def rotate_left(tree, rotation_root):
    """Vykona rotaci doleva kolem uzlu 'rotation_root' ve strome 'tree'."""
    pass


def rotate_right(tree, rotation_root):
    """Vykona rotaci doprava kolem uzlu 'rotation_root' ve strome 'tree'."""
    pass


def insert(tree, key):
    """Vlozi novy uzel s klicem 'key' do stromu 'tree'. Operace zachova
    korektni cerveno-cerny strom.
    """
    pass


def search(tree, key):
    """Vyhleda uzel s klicem 'key' ve strome 'tree'. Vrati uzel
    s hledanym klicem. Pokud se klic 'key' v strome nenachazi vraci None.
    """
    pass


def is_correct_rb_tree(tree):
    """Overi jestli je strom 'tree' korektni cerveno-cerny vyhledavaci
    strom. Pokud ano vraci True, jinak False.
    """
    pass


# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/ - zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graph(rbtree, filename):
    try:
        with open(filename, 'w') as f:
            f.write("digraph RBTree {\n")
            f.write("node [style=filled];\n")
            make_graphviz(rbtree.root, f)
            f.write("}\n")
        print("Vykresleny strom najdete v souboru", filename)
    except Exception:
        print("Ve vykreslovani nastala chyba")


def make_graphviz(node, f):
    if node is None:
        return

    if node.color == Colors.red:
        f.write('"{}" [color=red,label="{}"]\n'.format(id(node), node.key))
    elif node.color == Colors.black:
        f.write('"{}" [color=black,fontcolor=white,label="{}"]\n'
                .format(id(node), node.key))

    for child, lr in (node.left, 'L'), (node.right, 'R'):
        if child is not None:
            f.write('"{}" -> "{}"\n'.format(id(node), id(child)))
            make_graphviz(child, f)
        else:
            nil = lr + str(id(node))
            f.write('{} [label="",color=white]\n{} -> {}\n'
                    .format(nil, id(node), nil))


def init_rb_tree():
    tree = RedBlackTree()

    nodes = [Node() for _ in range(7)]

    for i in range(7):
        nodes[i].key = i

    tree.root = nodes[3]

    tree.root.left = nodes[1]
    nodes[1].parent = tree.root
    nodes[1].color = Colors.red
    nodes[1].left = nodes[0]
    nodes[0].parent = nodes[1]
    nodes[1].right = nodes[2]
    nodes[2].parent = nodes[1]

    tree.root.right = nodes[5]
    nodes[5].parent = tree.root
    nodes[5].left = nodes[4]
    nodes[5].color = Colors.red
    nodes[4].parent = nodes[5]
    nodes[5].right = nodes[6]
    nodes[6].parent = nodes[5]

    return tree


def init_unbalanced_tree_right():
    tree = RedBlackTree()

    nodes = [Node() for _ in range(7)]

    tree.root = nodes[0]
    for i in range(7):
        nodes[i].key = i
    for i in range(1, 7):
        nodes[i].parent = nodes[i - 1]
    for i in range(6):
        nodes[i].right = nodes[i + 1]

    return tree


def init_unbalanced_tree_left():
    tree = RedBlackTree()

    nodes = [Node() for _ in range(7)]

    tree.root = nodes[6]
    for i in range(7):
        nodes[i].key = i
    for i in range(6):
        nodes[i].parent = nodes[i + 1]
    for i in range(1, 7):
        nodes[i].left = nodes[i - 1]

    return tree


def helper_test_rotate_left(tree):
    rotate_left(tree, tree.root)

    if (tree.root.key != 1 or
            tree.root.left is None or
            tree.root.left.key != 0 or
            tree.root.right.key != 2):
        print("NOK - chybna rotace kolem korene stromu")
        return False

    rnode = tree.root.right
    rotate_left(tree, rnode)

    if (tree.root.right.key != 3 or
            tree.root.right.left is None or
            tree.root.right.left.right is not None or
            tree.root.right.left.key != 2 or
            tree.root.right.right.key != 4):
        print("NOK - chybna rotace kolem uzlu stromu")
        return False

    rnode = tree.root.left
    rotate_left(tree, rnode)

    if (rnode.left is not None or
            rnode.right is not None or
            tree.root.key != 1 or
            tree.root.left.key != 0):
        print("NOK - chybna rotace kolem uzlu bez potomka")
        return False

    rotate_left(tree, tree.root)

    if (tree.root.key != 3 or
            tree.root.right.key != 4 or
            tree.root.left.key != 1 or
            tree.root.left.right.key != 2):
        print("NOK - chybna rotace kolem korene stromu,",
              "testovani preveseni potomka")
        return False

    print("OK")
    return True


def test_rotate_left():
    print("Test 1. rotate_left: ")
    tree = init_unbalanced_tree_right()

    if not helper_test_rotate_left(tree):
        make_graph(tree, "rotate_left.dot")


def helper_test_rotate_right(tree):
    rotate_right(tree, tree.root)

    if (tree.root.key != 5 or
            tree.root.right is None or
            tree.root.right.key != 6 or
            tree.root.left.key != 4):
        print("NOK - chybna rotace kolem korene stromu")
        return False

    rnode = tree.root.left
    rotate_right(tree, rnode)

    if (tree.root.left.key != 3 or
            tree.root.left.right is None or
            tree.root.left.right.left is not None or
            tree.root.left.left.key != 2):
        print("NOK - chybna rotace kolem uzlu stromu")
        return False

    rnode = tree.root.right
    rotate_right(tree, rnode)

    if (tree.root.right.left is not None or
            tree.root.right.right is not None or
            tree.root.key != 5 or
            tree.root.right.key != 6):
        print("NOK - chybna rotace kolem uzlu bez potomka")
        return False

    rotate_right(tree, tree.root)

    if (tree.root.key != 3 or
            tree.root.left.key != 2 or
            tree.root.right.key != 5 or
            tree.root.right.left.key != 4):
        print("NOK - chybna rotace kolem korene stromu, ",
              "testovani preveseni potomka")
        return False

    print("OK")
    return True


def test_rotate_right():
    print("Test 2. rotate_right: ")
    tree = init_unbalanced_tree_left()

    if not helper_test_rotate_right(tree):
        make_graph(tree, "rotate_right.dot")


def helper_test_insert(tree):
    insert(tree, 5)

    if tree.root is None or tree.root.color != Colors.black:
        print("NOK - koren je cerveny")
        return False

    insert(tree, 9)

    if (tree.root.right is None or
            tree.root.right.color != Colors.red or
            tree.root.right.key != 9):
        print("NOK - chybne vlozeny cerveny uzel")
        return False

    insert(tree, 3)
    insert(tree, 4)

    if (tree.root.color != Colors.black or
            tree.root.right.color != Colors.black or
            tree.root.left.color != Colors.black or
            tree.root.left.right.color != Colors.red or
            tree.root.left.right.key != 4):
        print("NOK - chybne prebarveni a vkladani")
        return False

    insert(tree, 6)
    insert(tree, 7)

    if (tree.root.right.key != 7 or
            tree.root.right.left.key != 6 or
            tree.root.right.right.key != 9 or
            tree.root.right.color != Colors.black or
            tree.root.right.left.color != Colors.red or
            tree.root.right.right.color != Colors.red):
        print("NOK - chybna rotace vpravo s prebarvenim")
        return False

    insert(tree, 10)
    tnode = tree.root.right

    if (tnode.color != Colors.red or
            tnode.left.color != Colors.black or
            tnode.right.color != Colors.black or
            tnode.right.right.color != Colors.red or
            tnode.right.right.key != 10):
        print("NOK - chybne prebarveni bez rotace")
        return False

    insert(tree, 8)
    insert(tree, 12)
    r = tree.root

    if (r.key != 7 or
            r.left.key != 5 or
            r.left.right.key != 6 or
            r.right.left.key != 8 or
            r.right.right.right.key != 12 or
            r.color != Colors.black or
            r.left.color != Colors.red or
            r.right.color != Colors.red or
            r.left.right.color != Colors.black or
            r.right.left.color != Colors.black or
            r.right.right.right.color != Colors.red):
        print("NOK - chybna rotace kolem korene s prebarvenim")
        return False

    print("OK")
    return True


def test_insert():
    print("Test 3. insert: ")

    tree = RedBlackTree()

    if not helper_test_insert(tree):
        make_graph(tree, "insert.dot")


def helper_test_search(tree):
    node = search(tree, 3)

    if node is None or node.key != 3:
        print("NOK - chybne hledani korene s hodnotou 3")
        return False

    node = search(tree, 2)

    if node is None or node.key != 2:
        print("NOK - chybne hledani listu s hodnotou 2")
        return False

    node = search(tree, 7)

    if node is not None:
        print("NOK - hledani prvku, ktery se v strome nevyskytuje")
        return False

    print("OK")
    return True


def test_search():
    print("Test 4. search: ")

    tree = init_rb_tree()

    if not helper_test_search(tree):
        make_graph(tree, "search.dot")


def helper_test_is_correct_rb_tree_1(tree):
    if not is_correct_rb_tree(tree):
        print("NOK - strom je korektni")
        return False

    tree.root.color = Colors.red

    if is_correct_rb_tree(tree):
        print("NOK - strom ma cerveny koren")
        return False

    tree.root.color = Colors.black
    tree.root.left.color = Colors.black

    if is_correct_rb_tree(tree):
        print("NOK - strom nema stejnou cernou hloubku")
        return False

    return True


def helper_test_is_correct_rb_tree_2(tree):
    if not is_correct_rb_tree(tree):
        print("NOK - strom je korektni")
        return False

    n = Node()
    n.key = 0
    n.parent = tree.root
    tree.root.left = n

    if is_correct_rb_tree(tree):
        print("NOK - strom nema stejnou cernou hloubku")
        return False

    tree.root.left.color = Colors.red

    if not is_correct_rb_tree(tree):
        print("NOK - strom je korektni")
        return False

    print("OK")
    return True


def test_is_correct_rb_tree():
    print("Test 5. is_correct_rb_tree: ")

    tree = init_rb_tree()

    if not helper_test_is_correct_rb_tree_1(tree):
        make_graph(tree, "correct.dot")
        return

    tree = RedBlackTree()
    tree.root = Node()
    tree.root.key = 1

    if not helper_test_is_correct_rb_tree_2(tree):
        make_graph(tree, "correct.dot")


if __name__ == '__main__':
    test_rotate_left()
    test_rotate_right()
    test_insert()
    test_search()
    test_is_correct_rb_tree()
