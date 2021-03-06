#!/usr/bin/env python3

import heapq  # prioritni fronta
import math  # pro pouziti math.inf

# V teto uloze mate naimplementovat probirane algoritmy na nalezeni
# nejkratsich cest v grafu, tedy Dijkstruv a Belmannuv-Forduv algoritmus.
#
# Krome testu je pro vas i pripraven vypis v jazyce dot, staci z vaseho
# kodu zavolat funkci make_graph(graph, filename), ktere predate graf
# a jmeno souboru, do ktereho chcete graf vypsat.
#
# Knihovna heapq nabizi praci s prioritni frontou implementovanou pomoci
# minimove binarni haldy (ta je implementovana Pythonovskym seznamem). Prace s
# prioritni frontou je nasledujici:
#
# heapq.heappush(heap, item): prida prvek item do haldy heap (insert)
# heapq.heappop(heap): odebere minimalni prvek z haldy a vrati jej (extract)
#
# Knihovna heapq primo nepodporuje operaci decrease_key. Pro implementaci
# Dijkstrova algoritmu tedy budete muset pouzit jeho upravenou verzi (ktera se
# v praxi casto pouziva):
# - Misto decrease_key se vrchol do prioritni fronty vlozi s novou hodnotou.
# - Pri vybirani vrcholu ven z prioritni fronty je treba zjistit, jestli uz byl
#   zpracovan. Pokud byl, vrchol se zahodi a pokracuje se dal.
#   (Rozmyslete si, proc je tento pristup korektni!)
#
# Pro reprezentaci hodnot plus a minus nekonecno pouzijte math.inf a -math.inf.


class Graph:
    """Trida Graph slouzi k reprezentaci orientovaneho ohodnoceneho grafu.

    Atributy:
        size            pocet vrcholu grafu
        matrix          matice, ktera obsahuje hrany grafu
        distances       pole vzdalenosti ze zadaneho vrcholu
        predecessors    pole predchudcu, podle ktereho lze zpetne urcit,
                        kudy vedla cesta
    """

    def __init__(self, size):
        self.size = size
        self.matrix = [[math.inf] * size for _ in range(size)]
        self.distances = []
        self.predecessors = []


def is_edge(graph, u, v):
    """Pokud v zadanem grafu existuje hrana (u, v), vraci True, jinak False.
    """
    # TODO
    return graph.matrix[u][v]


def initialize(graph, s):
    """Funkce slouzi k inicializaci grafu. Nastavi vzdalenost inicialniho
    vrcholu 's' na 0 a zbytek na nekonecno. Predchudci vsech vrcholu jsou
    inicializovani na None.
    """
    # TODO
    for _ in range(graph.size):
        graph.predecessors.append(None)
    for i in range(graph.size):
        if i == s:
            graph.distances.append(0)
        else:
            graph.distances.append(math.inf)


def relax(graph, u, v):
    """Funkce slouzi k relaxaci hrany ('u', 'v') v orientovanem grafu 'graph'.
    Nezapomente pripadne nastavit predchudce vrcholu v.

    Volitelne: funke muze vracet True/False, podle toho, jestli doslo ke zmene
    v pomocnem poli 'distances'.
    (To se muze hodit pri implementaci algoritmu nize.)
    """
    # TODO
    graph.distances[v] = graph.distances[u] + graph.matrix[u][v]
    graph.predecessors[v] = u


def get_edges(graph):
    edges = []
    for i in range(graph.size):
        for j in range(graph.size):
            if graph.matrix[i][j] != math.inf:
                edges.append((i, j))
    return edges


def bellman_ford(graph, u, v):
    """Bellman-Forduv algoritmus pro nalezeni stromu nejkratsich cest
    z vrcholu 'u' v grafu 'graph'.

    Pokud graf obsahuje zaporny cyklus, funkce vraci None (obsah poli
    'graph.distances' a 'graph.predecessors' je irelevantni).

    V opacnem pripade funkce vraci delku cesty z 'u' do 'v' (nekonecno, pokud
    zadna cesta neexistuje), v poli 'graph.distances' budou po vypoctu
    vzdalenosti vrcholu od 'u' a v poli 'graph.predecessors' budou prechudci
    vrcholu na nejkratsi ceste z 'u'.
    """
    # TODO
    initialize(graph, u)
    edges = get_edges(graph)
    for i in range(graph.size - 1):
        pre_end = True
        for a, b in edges:
            if graph.distances[b] > graph.distances[a] + graph.matrix[a][b]:
                relax(graph, a, b)
                pre_end = False
        if pre_end:
            break
    for a, b in edges:
        if graph.distances[b] > graph.distances[a] + graph.matrix[a][b]:
            return None
    return graph.distances[v]


def get_neighbors(graph, u):
    neighbors = []
    for i in range(graph.size):
        if graph.matrix[u][i] != math.inf:
            neighbors.append(i)
    return neighbors


def dijkstra(graph, u, v):
    """Dijkstruv algoritmus pro nalezeni nejkratsich cest z vrcholu 'u' v grafu
    'graph'. Predpokladame, ze graf obsahuje pouze nezaporne ohodnocene hrany.

    Funkce vraci delku cesty z 'u' do 'v' (nekonecno, pokud zadna cesta
    neexistuje), v poli 'graph.distances' budou po vypoctu vzdalenosti vrcholu
    od 'u' a v poli 'graph.predecessors' budou prechudci vrcholu na nejkratsi
    ceste z 'u'.

    O pouziti knihovny heapq se doctete v komentarich vyse.

    Hint: Do prioritni fronty budete muset ukladat dvojice, ne jen vrcholy.
    """
    # TODO
    initialize(graph, u)
    pairs = [(graph.distances[i], i) for i in range(graph.size)]
    Q = []
    for i in range(graph.size):
        heapq.heappush(Q, pairs[i])
    while Q:
        a_dist, a = heapq.heappop(Q)
        if a_dist == math.inf:
            continue
        neighbors = get_neighbors(graph, a)
        for b in neighbors:
            if graph.distances[b] > a_dist + graph.matrix[a][b]:
                relax(graph, a, b)
                heapq.heappush(Q, (graph.distances[b], b))
    return graph.distances[v]


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
def make_graph(graph, filename):
    with open(filename, 'w') as f:
        f.write("digraph MyGraph {\n")
        make_graphviz(graph, f)
        f.write("}\n")


def make_graphviz(graph, f):
    for u in range(graph.size):
        for v in range(graph.size):
            if graph.matrix[u][v] != math.inf:
                f.write('"{}" -> "{}" [label="{}"]\n'
                        .format(u, v, graph.matrix[u][v]))


def add_edge(graph, u, v, w):
    """Prida hranu ('u', 'v') vahy 'w' do zadaneho grafu.
    Funkce nic nedela v pripade, ze 'u' nebo 'v' je mimo rozsah grafu.
    """
    if u >= 0 and v >= 0 and u < graph.size and v < graph.size:
        graph.matrix[u][v] = w


def print_matrix(graph):
    for i in range(graph.size):
        for j in range(graph.size):
            print("{0:4} ".format(graph.matrix[i][j]), end="")
        print("")


def create_test_graph():
    graph = Graph(6)
    for u, v, w in ((0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 3, 15), (1, 2, 10),
                    (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9), (1, 0, 7),
                    (2, 0, 9), (5, 0, 14), (3, 1, 15), (2, 1, 10), (3, 2, 11),
                    (5, 2, 2), (4, 3, 6), (5, 4, 9)):
        add_edge(graph, u, v, w)

    return graph


def test_initialize():
    print("Test 1. initialize: ")

    graph1 = Graph(1)
    initialize(graph1, 0)
    if graph1.distances != [0] or graph1.predecessors != [None]:
        print("NOK - initialize nefunguje jak ma na grafu o velikosti 1.")
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return False

    graph2 = create_test_graph()
    initialize(graph2, 2)
    if graph2.distances != [math.inf] * 2 + [0] + [math.inf] * 3 or \
       graph2.predecessors != [None] * 6:
        print("NOK - init nefunguje jak ma na grafu o velikosti 6.")
        print("Matice vypada takto:")
        print_matrix(graph2)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph2.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph2.predecessors)
        return False

    print("OK")
    return True


def test_relax():
    print("Test 2. funkce relax: ")

    graph1 = create_test_graph()
    initialize(graph1, 0)
    relax(graph1, 0, 1)
    if graph1.distances[1] != 7 or graph1.predecessors[1] != 0:
        print("NOK - relax nefunguje jak ma na testovacim grafu ", end="")
        print("pri volani na vrcholy 0 1")
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return

    graph2 = create_test_graph()
    initialize(graph2, 2)
    relax(graph2, 2, 0)
    relax(graph2, 0, 1)
    relax(graph2, 2, 1)
    if graph2.distances[1] != 10 or graph2.predecessors[1] != 2:
        print("NOK - init nefunguje jak ma na grafu o velikosti 6.")
        print("posloupnost provedenych akci - 1. initialize(g, 2):")
        tmp_graph = create_test_graph()
        initialize(tmp_graph, 2)
        print("Matice vypada takto:")
        print_matrix(tmp_graph)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)

        print("\n2. relax(g, 2, 0):")
        relax(tmp_graph, 2, 0)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)

        print("\n3. relax(g, 0, 1):")
        relax(tmp_graph, 0, 1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)

        print("\n4. relax(g, 2, 1):")
        relax(tmp_graph, 2, 1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)
        return

    print("OK")


def test_bellman_ford():
    print("Test 3. Bellman-Forduv algoritmus: ")

    graph1 = Graph(5)
    add_edge(graph1, 0, 1, 1)
    ret = bellman_ford(graph1, 0, 1)
    if ret != 1:
        print("NOK - cesta z 0 do 1 ma delku 1.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return

    graph2 = Graph(5)
    add_edge(graph2, 0, 1, 1)
    ret = bellman_ford(graph2, 1, 2)
    if ret != math.inf:
        print("NOK - cesta z 1 do 2 neexistuje (delka je nekonecno).")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph2)
        print("Seznam vzdalenosti z vrcholu 1 vypada takto:")
        print(graph2.distances)
        print("Seznam predchudcu na ceste z vrcholu 1 vypada takto:")
        print(graph2.predecessors)
        return

    graph3 = Graph(1)
    ret = bellman_ford(graph3, 0, 0)
    if ret != 0:
        print("NOK - cesta z 0 do 0 ma delku 0.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph3)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph3.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph3.predecessors)
        return

    graph4 = create_test_graph()
    ret = bellman_ford(graph4, 0, 4)
    if ret != 20:
        print("NOK - cesta z 0 do 4 ma delku 20.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph4)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph4.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph4.predecessors)
        return

    graph5 = create_test_graph()
    add_edge(graph5, 3, 4, -1)
    ret = bellman_ford(graph5, 0, 4)
    if ret != 19:
        print("NOK - cesta z 0 do 4 ma delku 19.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph5)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph5.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph5.predecessors)
        return

    graph6 = create_test_graph()
    add_edge(graph6, 3, 4, -7)
    ret = bellman_ford(graph6, 0, 4)
    if ret is not None:
        print("NOK - graf obsahuje zaporny cyklus")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph6)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph6.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph6.predecessors)
        return

    print("OK")


def test_dijkstra():
    print("Test 4. Dijkstruv algoritmus: ")

    graph1 = Graph(5)
    add_edge(graph1, 0, 1, 1)
    ret = dijkstra(graph1, 0, 1)
    if ret != 1:
        print("NOK - cesta z 0 do 1 ma delku 1.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return

    graph2 = Graph(5)
    add_edge(graph2, 0, 1, 1)
    ret = dijkstra(graph2, 1, 2)
    if ret != math.inf:
        print("NOK - cesta z 1 do 2 neexistuje (delka je nekonecno).")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph2)
        print("Seznam vzdalenosti z vrcholu 1 vypada takto:")
        print(graph2.distances)
        print("Seznam predchudcu na ceste z vrcholu 1 vypada takto:")
        print(graph2.predecessors)
        return

    graph3 = Graph(1)
    ret = dijkstra(graph3, 0, 0)
    if ret != 0:
        print("NOK - cesta z 0 do 0 ma delku 0.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph3)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph3.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph3.predecessors)
        return

    graph4 = create_test_graph()
    ret = dijkstra(graph4, 0, 4)
    if ret != 20:
        print("NOK - cesta z 0 do 4 ma delku 20.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph4)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph4.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph4.predecessors)
        return

    print("OK")


if __name__ == '__main__':
    if test_initialize():
        test_relax()
        test_bellman_ford()
        test_dijkstra()
    # make_graph(create_test_graph(), "test13.dot")
