#!/usr/bin/env python3
import sys
from io import StringIO


class Node:
    """Trida Node slouzi k reprezentaci uzlu v B-strome.

    Atributy:
        keys        pole obsahujici klice daneho uzlu
        children    pole obsahujici reference na potomky
        leaf        urcuje, zdali je uzel list

    Poznamka: Narozdil od implementace z prednasky/sbirky zde nepouzivame pole
    pevne delky, ale Pythonovske seznamy, ktere muzeme zvetsovat pomoci
    seznam.append(prvek) a zmensovat pomoci seznam.pop().
    Z tohoto duvodu rovnez trida Node neobsahuje atribut n (pocet klicu),
    protoze pocet klicu muzeme snadno zjistit pomoci len(node.keys).
    """

    def __init__(self):
        self.keys = []
        self.children = []
        self.leaf = False


class BTree:
    """Trida BTree slouzi k reprezentaci B-stromu

    Atributy:
        arity   pocet maximalnich potomku uzlu (stupen B-stromu je arity // 2)
        root    koren B-stromu
    """

    def __init__(self):
        self.arity = 0
        self.root = None


def node_in_order_print(node):
    if node.leaf:
        for key in node.keys:
            print(key, end=" ")
    else:
        len_keys = len(node.keys)
        for i in range(len_keys):
            node_in_order_print(node.children[i])
            print(node.keys[i], end=" ")
        node_in_order_print(node.children[len_keys])


def in_order_print(tree):
    """Vypise B-strom 'tree' pomoci inorder pruchodu. Pro vypis
    pouzivejte print. Hodnoty odsazujte mezerami nebo odradkovanim.
    """
    # TODO
    if tree.root is not None:
        node_in_order_print(tree.root)


def node_pre_order_print(node):
    if node.leaf:
        for key in node.keys:
            print(key, end=" ")
    else:
        len_keys = len(node.keys)
        for key in node.keys:
            print(key, end=" ")
        for i in range(len_keys + 1):
            node_pre_order_print(node.children[i])


def pre_order_print(tree):
    """Vypise B-strom 'tree' pomoci preorder pruchodu. Pro vypis
    pouzivejte print. Hodnoty odsazujte mezerami nebo odradkovanim.
    """
    # TODO
    if tree.root is not None:
        node_pre_order_print(tree.root)


def node_post_order_print(node):
    if node.leaf:
        for key in node.keys:
            print(key, end=" ")
    else:
        len_keys = len(node.keys)
        for i in range(len_keys + 1):
            node_post_order_print(node.children[i])
        for key in node.keys:
            print(key, end=" ")


def post_order_print(tree):
    """Vypise B-strom 'tree' pomoci postorder pruchodu. Pro vypis
    pouzivejte print. Hodnoty odsazujte mezerami nebo odradkovanim.
    """
    # TODO
    if tree.root is not None:
        node_post_order_print(tree.root)


def binary_search_key_in_node(node, key):
    array = node.keys
    lena = len(array)
    low = 0
    high = lena - 1
    mid = (low + high) // 2
    while low <= high:
        if node.keys[mid] == key:
            return mid, True
        if node.keys[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return mid + 1, False


def search_key_in_node(node, key):
    array = node.keys
    lena = len(array)
    i = 0
    while i < lena and array[i] < key:
        i += 1
    if i < lena and array[i] == key:
        return i, True
    return i, False


def search(tree, key):
    """Vyhleda uzel s klicem 'key' v B-strome 'tree'. Vrati uzel, ve
    kterem se nachazi klic. Pokud se klic 'key' v B-strome nenachazi,
    vraci None.
    """
    # TODO
    if tree.root is None:
        return None
    node = tree.root
    children_index, key_in_node = binary_search_key_in_node(node, key)
    while not key_in_node and not node.leaf:
        node = node.children[children_index]
        children_index, key_in_node = binary_search_key_in_node(node, key)
    if key_in_node:
        return node
    return None


class Item:
    """Trida Item slouzi pro reprezentaci objektu ve fronte.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        left    reference na dalsi prvek ve fronte
    """
    def __init__(self):
        self.value = None
        self.left = None


class Queue:
    """Trida Queue reprezentuje frontu.

    Atributy:
        atribut first je reference na prvni prvek
        atribut last je reference na posledni prvek
    """
    def __init__(self):
        self.first = None
        self.last = None


def enqueue(queue, value):
    """Metoda enqueue vlozi do fronty (queue) novy prvek s hodnotou
    (value).
    """
    # TODO
    new = Item()
    new.value = value
    new.left = None
    if isEmpty(queue):
        queue.first = new
        queue.last = new
    else:
        queue.last.left = new
        queue.last = new

def dequeue(queue):
    """Metoda dequeue odebere prvni prvek z fronty (queue).
    Vraci hodnotu (value) odebraneho prvku, pokud je fronta prazdna,
    vraci None
    """
    # TODO
    theNode = queue.first
    if isEmpty(queue):
        return None
    elif queue.first is queue.last:
        queue.last = None
        queue.first = None
    else:
        queue.first = queue.first.left
        theNode.left = None
    return theNode.value

def isEmpty(queue):
    """isEmpty() vraci True v pripade prazdne fronty, jinak False."""
    # TODO
    return queue.last is None


def are_equal(array1, array2):
    lena1 = len(array1)
    lena2 = len(array2)
    if lena1 != lena2:
        return False
    for i in range(lena1):
        if array1[i] != array2[i]:
            return False
    return True


def is_equiv(tree1, tree2):
    """Overi, jestli jsou 2 B-stromy ekvivalentni. Pokud ano, vraci
    True, jinak False.
    """
    # TODO
    if tree1.root is None and tree2.root is None:
        return True
    if tree1.root is None:
        return False
    if tree2.root is None:
        return False
    queue1 = Queue()
    queue2 = Queue()
    enqueue(queue1, tree1.root)
    enqueue(queue2, tree2.root)
    while not isEmpty(queue1) and not isEmpty(queue2):
        node1 = queue1.first.value
        node2 = queue2.first.value
        len_children1 = len(node1.children)
        len_children2 = len(node2.children)
        if len_children1 != len_children2:
            return False
        if not are_equal(node1.keys, node2.keys):
            return False
        for i in range(len_children1):
            enqueue(queue1, node1.children[i])
        for i in range(len_children2):
            enqueue(queue2, node2.children[i])
        dequeue(queue1)
        dequeue(queue2)
    return isEmpty(queue1) and isEmpty(queue2)


# inserts key to non-full node
def insert_to_leaf(leaf, key):
    pos, key_in_leaf = binary_search_key_in_node(leaf, key)
    if not key_in_leaf:
        leaf.keys.append(key)
        len_keys = len(leaf.keys)
        for i in range(len_keys - 1, pos, -1):
            leaf.keys[i] = leaf.keys[i - 1]
        leaf.keys[pos] = key


def split_root(root):
    len_keys = len(root.keys)
    split_index = len_keys // 2
    new_node1 = Node()
    new_node2 = Node()

    if root.leaf:
        new_node1.children = []
        new_node2.children = []
    else:
        new_node1.children = root.children[0:split_index + 1]
        new_node2.children = root.children[split_index + 1:len_keys + 1]

    new_node1.leaf = root.leaf
    new_node1.keys = root.keys[0:split_index]

    new_node2.leaf = root.leaf
    new_node2.keys = root.keys[split_index + 1:len_keys]

    root.keys = [root.keys[split_index]]
    root.children = [new_node1, new_node2]
    root.leaf = False


# it is guaranteed that parent is not full, so +1 won't do any harm
def split_node(node, parent, child_index):
    new_node = Node()
    new_node.leaf = node.leaf
    mid = len(node.keys) // 2
    tmp_key = node.keys[mid]
    # copy second half of keys
    for i in range(0, mid):
        new_node.keys.append(node.keys[mid + 1 + i])
    # copy second half of children
    if not node.leaf:
        for i in range(0, mid + 1):
            new_node.children.append(node.children[mid + 1 + i])
    # cut the node to contain only the first half
    node.keys = node.keys[0:mid]
    node.children = node.children[0:mid + 1]
    # RESOLVE THE PARENT
    # increase size of keys
    parent.keys.append(tmp_key)
    len_keys = len(parent.keys)
    # reorganize array of keys
    for i in range(len_keys - 1, child_index, -1):
        parent.keys[i] = parent.keys[i - 1]
    # insert the key
    parent.keys[child_index] = tmp_key
    # increase size of children
    parent.children.append(new_node)
    len_children = len(parent.children)
    # reorganize array of children
    for i in range(len_children - 1, child_index + 1, -1):
        parent.children[i] = parent.children[i - 1]
    # insert the new child
    parent.children[child_index + 1] = new_node


def node_insert(root, key, max_keys):
    node = root
    while not node.leaf:
        child_index, key_in_node = binary_search_key_in_node(node, key)
        if key_in_node:
            return
        child = node.children[child_index]
        if len(child.keys) == max_keys:
            split_node(child, node, child_index)
            if key <= node.keys[child_index]:
                node = child
            else:
                node = node.children[child_index + 1]
        else:
            node = child
    insert_to_leaf(node, key)


def insert(tree, key):
    """Vlozi klic 'key' do B-stromu 'tree'. Operace implementuje
    preemptivne stepeni. Muzete predpokladat, ze B-strom ma sudou aritu.
    """
    # TODO
    if tree.root is None:
        tree.root = Node()
        tree.root.leaf = True
        tree.root.keys.append(key)
    else:
        if len(tree.root.keys) == tree.arity - 1:
            split_root(tree.root)
        node_insert(tree.root, key, tree.arity - 1)


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
def make_graphviz(node, i, f, arity):
    if node is None:
        return
    f.write('node{} [label = "'.format(i))
    for key in enumerate(node.keys):
        f.write("<f{}> |{}| ".format(key[0], key[1]))
    f.write('<f{}>"];\n'.format(len(node.keys)))

    for child in enumerate(node.children):
        make_graphviz(child[1], (i + 1) * arity + child[0], f, arity)

    if node.children:
        for j in range(len(node.children)):
            value = (i + 1) * arity + j
            f.write('"node{}":f{} -> "node{}"\n'.format(i, j, value))


def make_graph(tree, filename):
    try:
        with open(filename, 'w') as f:
            f.write("digraph BTree {\n")
            f.write("node [shape = record];\n")
            make_graphviz(tree.root, 0, f, tree.arity)
            f.write("}\n")
        print("Vykresleny B-strom najdete v souboru", filename)
    except Exception:
        print("Ve vykreslovani nastala chyba")


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().split())
        sys.stdout = self._stdout


def create_node(keys, children):
    node = Node()
    node.children = children
    node.keys = keys
    node.leaf = len(children) == 0
    return node


def test_tree_1():
    tree = BTree()
    tree.arity = 6

    n1 = create_node([1, 8, 12, 16, 25], [])

    tree.root = n1
    return tree


def test_tree_2():
    tree = BTree()
    tree.arity = 4

    n12 = create_node([55, 75], [])
    n11 = create_node([25], [])
    n10 = create_node([17], [])
    n9 = create_node([14, 15], [])
    n8 = create_node([9, 10, 12], [])
    n7 = create_node([6, 7], [])
    n6 = create_node([3], [])
    n5 = create_node([0, 1], [])
    n4 = create_node([16, 18, 50], [n9, n10, n11, n12])
    n3 = create_node([8], [n7, n8])
    n2 = create_node([2], [n5, n6])
    n1 = create_node([5, 13], [n2, n3, n4])

    tree.root = n1

    return tree


def test_tree_3():
    tree = BTree()
    tree.arity = 8

    n9 = create_node([66, 67, 68, 69, 70, 73, 79], [])
    n8 = create_node([40, 42, 47, 48, 50, 52, 56], [])
    n7 = create_node([36, 37, 38], [])
    n6 = create_node([29, 31, 32, 33, 34], [])
    n5 = create_node([23, 24, 27], [])
    n4 = create_node([18, 19, 20, 21], [])
    n3 = create_node([13, 15, 16], [])
    n2 = create_node([1, 3, 8], [])
    n1 = create_node([12, 17, 22, 28, 35, 39, 65],
                     [n2, n3, n4, n5, n6, n7, n8, n9])

    tree.root = n1
    return tree


def test_tree_4():
    tree = BTree()
    tree.arity = 4

    n12 = create_node([55, 75], [])
    n11 = create_node([25], [])
    n10 = create_node([17], [])
    n9 = create_node([14, 15], [])
    n8 = create_node([9, 10, 12], [])
    n7 = create_node([5, 7], [])
    n6 = create_node([3], [])
    n5 = create_node([0, 1], [])
    n4 = create_node([16, 19, 50], [n9, n10, n11, n12])
    n3 = create_node([8], [n7, n8])
    n2 = create_node([2], [n5, n6])
    n1 = create_node([5, 13], [n2, n3, n4])

    tree.root = n1

    return tree


def capture(fun, tree):
    with Capturing() as output:
        fun(tree)

    return list(map(int, output))


def test_in_order_print():
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 1. in_order_print: ")

    tree = helper_test_in_order_print()
    if tree is not None:
        make_graph(tree, "in_order.dot")


def helper_test_in_order_print():
    res1 = [1, 8, 12, 16, 25]
    res2 = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18,
            25, 50, 55, 75]
    res3 = [1, 3, 8, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27,
            28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 47, 48,
            50, 52, 56, 65, 66, 67, 68, 69, 70, 73, 79]

    tree = test_tree_1()
    res = capture(in_order_print, tree)

    if res1 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res1))
        return tree

    tree = test_tree_2()
    res = capture(in_order_print, tree)

    if res2 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res2))
        return tree

    tree = test_tree_3()
    res = capture(in_order_print, tree)

    if res3 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res3))
        return tree

    print("OK")


def test_pre_order_print():
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 2. pre_order_print: ")

    tree = helper_test_pre_order_print()
    if tree is not None:
        make_graph(tree, "pre_order.dot")


def helper_test_pre_order_print():
    res1 = [1, 8, 12, 16, 25]
    res2 = [5, 13, 2, 0, 1, 3, 8, 6, 7, 9, 10, 12, 16, 18, 50, 14, 15,
            17, 25, 55, 75]
    res3 = [12, 17, 22, 28, 35, 39, 65, 1, 3, 8, 13, 15, 16, 18, 19, 20,
            21, 23, 24, 27, 29, 31, 32, 33, 34, 36, 37, 38, 40, 42, 47,
            48, 50, 52, 56, 66, 67, 68, 69, 70, 73, 79]

    tree = test_tree_1()
    res = capture(pre_order_print, tree)

    if res1 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res1))
        return tree

    tree = test_tree_2()
    res = capture(pre_order_print, tree)

    if res2 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res2))
        return tree

    tree = test_tree_3()
    res = capture(pre_order_print, tree)

    if res3 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res3))
        return tree

    print("OK")


def test_post_order_print():
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 3. post_order_print: ")

    tree = helper_test_post_order_print()
    if tree is not None:
        make_graph(tree, "post_order.dot")


def helper_test_post_order_print():
    res1 = [1, 8, 12, 16, 25]
    res2 = [0, 1, 3, 2, 6, 7, 9, 10, 12, 8, 14, 15, 17, 25, 55, 75, 16,
            18, 50, 5, 13]
    res3 = [1, 3, 8, 13, 15, 16, 18, 19, 20, 21, 23, 24, 27, 29, 31, 32,
            33, 34, 36, 37, 38, 40, 42, 47, 48, 50, 52, 56, 66, 67, 68,
            69, 70, 73, 79, 12, 17, 22, 28, 35, 39, 65]

    tree = test_tree_1()
    res = capture(post_order_print, tree)

    if res1 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res1))
        return tree

    tree = test_tree_2()
    res = capture(post_order_print, tree)

    if res2 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res2))
        return tree

    tree = test_tree_3()
    res = capture(post_order_print, tree)

    if res3 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res3))
        return tree

    print("OK")


def test_search():
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 4. search: ")
    tree = helper_test_search()
    if tree is not None:
        make_graph(tree, "search.dot")


def helper_test_search():
    tree = test_tree_1()

    node = search(tree, 16)
    if node is None or 16 not in node.keys:
        print("NOK - chybne hledani klice 16, ktery je v koreni B-stromu")
        return tree

    node = search(tree, 24)
    if node is not None:
        print("NOK - chybne hledani klice, ktery se v B-strome nenachazi")
        return tree

    tree = test_tree_2()

    node = search(tree, 15)
    if node is None or 15 not in node.keys:
        print("NOK - chybne hledani klice 15, ktery je v listu")
        return tree

    node = search(tree, 50)
    if node is None or 50 not in node.keys:
        print("NOK - chybne hledani klice 50, ktery je ve vnitrnim uzlu")
        return tree

    node = search(tree, 19)
    if node is not None:
        print("NOK - chybne hledani klice, ktery se v B-strome nenachazi")
        return tree

    print("OK")


def test_is_equiv():
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 5. is_equiv: ")

    trees = helper_test_is_equiv()
    if trees is not None:
        make_graph(trees[0], "t1.dot")
        make_graph(trees[1], "t2.dot")


def helper_test_is_equiv():
    t1 = test_tree_1()
    t2 = test_tree_2()

    if is_equiv(t1, t2):
        print("NOK - B-stromy nejsou ekvivalentni, nemaji shodnou aritu")
        return t1, t2

    t1 = test_tree_2()
    t2 = test_tree_4()

    if is_equiv(t1, t2):
        print("NOK - B-stromy nejsou ekvivalentni, nemaji shodne hodnoty")
        return t1, t2

    t1 = test_tree_2()
    t2 = test_tree_2()

    if not is_equiv(t1, t2):
        print("NOK - B-stromy jsou ekvivalentni")
        return t1, t2

    print("OK")


def test_insert():
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 6. insert: ")

    tree = helper_test_insert()
    if tree is not None:
        make_graph(tree, "insert.dot")


def helper_test_insert():
    tree = BTree()
    tree.arity = 4

    insert(tree, 1)

    if (tree.root is None) or (tree.root.keys != [1]):
        print("NOK - vkladani do prazdneho B-stromu stupne 2")
        return tree

    insert(tree, 7)
    insert(tree, 2)

    if (tree.root is None) or (tree.root.keys != [1, 2, 7]):
        print("NOK - vkladani do B-stromu bez stepeni")
        return tree

    insert(tree, 5)

    if (tree.root is None or
            tree.root.keys != [2] or
            tree.root.children[0].keys != [1] or
            tree.root.children[1].keys != [5, 7]):
        print("NOK - vkladani se stepenim korene")
        return tree

    insert(tree, 12)
    insert(tree, 8)

    if (tree.root is None or
            tree.root.keys != [2, 7] or
            tree.root.children[0].keys != [1] or
            tree.root.children[1].keys != [5] or
            tree.root.children[2].keys != [8, 12]):
        print("NOK - vkladani se stepenim listu")
        return tree

    insert(tree, 4)
    insert(tree, 3)
    insert(tree, 6)

    if (tree.root is None or
            tree.root.keys != [2, 4, 7] or
            tree.root.children[1].keys != [3] or
            tree.root.children[2].keys != [5, 6] or
            tree.root.children[3].keys != [8, 12]):
        print("NOK - vkladani se stepenim listu")
        return tree

    insert(tree, 11)

    if (tree.root is None or
            tree.root.keys != [4] or
            tree.root.children[0].keys != [2] or
            tree.root.children[1].keys != [7] or
            tree.root.children[1].children[0].keys
            != [5, 6] or
            tree.root.children[1].children[1].keys
            != [8, 11, 12]):
        print("NOK - vkladani se stepenim korene")
        return tree

    print("OK")


if __name__ == '__main__':
    test_in_order_print()
    test_pre_order_print()
    test_post_order_print()
    test_search()
    test_is_equiv()
    test_insert()
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")