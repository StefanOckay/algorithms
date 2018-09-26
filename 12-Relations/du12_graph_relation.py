#!/usr/bin/env python3

# Povolene knihovny: copy, math, collections

# IB002 Domaci uloha 12.
#
# S relacemi se vetsina z vas setkala na predmetu Matematicke zaklady
# informatiky. Relace na mnozine intuitivne popisuje vztah mezi prvky
# teto mnoziny. Mejme treba relaci "byt kamaradem", kdy prvky A a B
# (z mnoziny lidi) jsou v relaci, pokud A je kamaradem B.
# Orientovany graf lze chapat jako (binarni) relaci mezi prvky, kde uzly
# reprezentuji prvky mnoziny a z uzlu A do B vede hrana, prave kdyz je
# A v relaci s B.

# Mezi zakladni vlastnosti binarnich relaci patri:
#
# *reflexivita*
# Relace je reflexivni, pokud je kazdy prvek v relaci sam se sebou.
#
# *symetrie*
# Relace je symetricka, pokud pro libovolne dva prvky A a B plati:
# Pokud A je v relaci s B, pak je taky B v relaci s A.
#
# *antisymetrie*
# Relace je antisymetricka, pokud pro libovolne dva ruzne prvky A a B plati:
# Pokud A je v relaci s B, pak B neni v relaci s A.
#
# *tranzitivita*
# Relace je tranzitivni, pokud pro libovolne prvky A, B, C plati:
# Je-li A v relaci s B a B je v relaci s C, pak taky A je v relaci s C.


# Nasledujici definici tridy Graph nijak nemodifikujte.
# Reprezentace grafu je stejna jako v minulem du.

from collections import deque


class Graph:
    """Trida Graph drzi graf reprezentovany matici sousednosti.
    Atributy:
        size: velikost (pocet vrcholu) grafu
        matrix: matice sousednosti
                [u][v] reprezentuje hranu u -> v
                (True: hrana existuje, False: hrana neexistuje)
    """

    def __init__(self, size):
        self.size = size
        self.matrix = [[False] * size for _ in range(size)]


# Ukol 1.
# Implementujte funkce is_reflexive, is_symmetric, is_antisymmetric
# a is_transitive, ktere pro vstupni graf overi, zda jim reprezentovana relace
# splnuje podminky dane vlastnosti.

def is_reflexive(graph):
    """Zjisti, zda je relace zadana grafem reflexivni.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    # TODO
    for i in range(graph.size):
        if not graph.matrix[i][i]:
            return False
    return True


def is_symmetric(graph):
    """Zjisti, zda je relace zadana grafem symetricka.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    # TODO
    for i in range(graph.size):
        for j in range(i + 1, graph.size):
            if graph.matrix[i][j] is not graph.matrix[j][i]:
                return False
    return True


def is_antisymmetric(graph):
    """Zjisti, zda je relace zadana grafem antisymetricka.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    # TODO
    for i in range(graph.size):
        for j in range(i + 1, graph.size):
            if graph.matrix[i][j] is graph.matrix[j][i]:
                return False
    return True


def is_transitive(graph):
    """Zjisti, zda je relace zadana grafem tranzitivni.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n^3), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    # TODO
    for i in range(graph.size):
        for j in range(graph.size):
            if graph.matrix[i][j]:
                for k in range(graph.size):
                    if graph.matrix[j][k]:
                        if not graph.matrix[i][k]:
                            return False
    return True


# Ukol 2.
# Implementujte funkci transitive_closure, ktera spocita tranzitivni
# uzaver daneho grafu. Tranzitivni uzaver je nejmensi nadmnozina relace,
# ktera splnuje podminky pro tranzitivitu (relace je chapana jako mnozina
# vsech dvojic, ktere jsou v dane relaci).
#
# Tranzitivni uzaver grafu lze taky definovat jako graf, ve kterem vede
# hrana z vrcholu A do vrcholu B, pokud v puvodnim grafu existovala
# nejaka orientovana cesta vedouci z vrcholu A do vrcholu B.
#
# Puvodni graf nemente, vytvorte si kopii.

def convert_to_list(graph):
    """Vytvori seznam nasledniku z grafu zadaneho matici sousednosti 'matrix'.
    V seznamech nasledniku se vyskytuji indexy sousedu, nic jineho.
    Pokud vrchol nema nasledniky, je jeho seznam nasledniku prazdny.
    Pro implementaci seznamu pouzijte bezne Pythonovske seznamy.

    Napr. pro graf zadany matici:
        0 0 1
        1 1 1
        0 0 0
    ma byt vysledkem [[2], [0, 1, 2], []]
    """
    # TODO
    result = []
    for i in range(graph.size):
        vertex_neighbors = []
        for j in range(graph.size):
            if graph.matrix[i][j]:
                vertex_neighbors.append(j)
        result.append(vertex_neighbors)
    return result


def reachable_from(start, graph):
    succ_list = convert_to_list(graph)
    queue = deque()
    queue.append(start)
    distance = [None for _ in range(graph.size)]
    distance[start] = 0
    reachables = []
    while queue:
        node = queue.popleft()
        for i in range(len(succ_list[node])):
            next_node = succ_list[node][i]
            if distance[next_node] is None or distance[next_node] == 0:
                reachables.append(next_node)
                distance[next_node] = distance[node] + 1
                queue.append(next_node)
    return reachables


def transitive_closure(graph):
    """Vypocita tranzitivni uzaver zadaneho grafu.
    Vstup: graph - orientovany graf typu Graph
    Vystup: tranzitivni uzaver grafu (objekt typu Graph)
    casova slozitost: O(n^3), kde n je pocet vrcholu grafu
    """
    # TODO
    new_graph = Graph(graph.size)
    for i in range(graph.size):
        for j in range(graph.size):
            new_graph.matrix[i][j] = graph.matrix[i][j]
    for i in range(new_graph.size):
        reachables = reachable_from(i, graph)
        for j in range(len(reachables)):
            new_graph.matrix[i][reachables[j]] = True
    return new_graph



graph1 = Graph(3)

graph1.matrix[0][0] = False
graph1.matrix[0][1] = True
graph1.matrix[0][2] = False

graph1.matrix[1][0] = False
graph1.matrix[1][1] = False
graph1.matrix[1][2] = True

graph1.matrix[2][0] = False
graph1.matrix[2][1] = True
graph1.matrix[2][2] = False

graph2 = Graph(1)

graph2.matrix[0][0] = True

print(is_antisymmetric(graph2))

print(is_reflexive(graph1))
print(is_symmetric(graph1))
print(is_antisymmetric(graph1))
print(is_transitive(graph1))

print(transitive_closure(graph1).matrix)

graph3 = Graph(2)

graph3.matrix[0][0] = False
graph3.matrix[0][1] = True
graph3.matrix[1][0] = True
graph3.matrix[1][1] = False

print(is_transitive(graph3))
print(transitive_closure(graph3).matrix)
