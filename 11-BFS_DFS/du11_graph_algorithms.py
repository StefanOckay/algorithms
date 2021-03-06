#!/usr/bin/env python3

# Povolene knihovny: copy, math, collections
# Z knihovny collections se vam muze hodit datova struktura deque:

from collections import deque

# IB002 Domaci uloha 11.
#
# Tento tyden bude vasim ukolem implementovat dva grafove algoritmy.
# Ukoly jsou zamereny na aplikace pruchodu grafem.
#
# Reprezentace grafu je stejna jako v ukolu cv11, tedy matici sousednosti.
# Matice je indexovana od [0][0], vrcholum odpovidaji cisla 0 .. graph.size-1.
# V matici je na indexu [u][v] hodnota True, pokud graf obsahuje hranu u -> v,
# jinak je tam hodnota False.
#
# Grafy (i neorientovane!) mohou obsahovat smycky (tj. situace, kdy v matici
# na indexu [u][u] je True) a mohou byt i nesouvisle.
#
# Pripomenuti prace s frontou typu deque:
# inicializace fronty: queue = deque() nebo queue = deque([seznam prvku])
# vlozeni prvku do fronty: queue.append(prvek)
# vybrani prvku z fronty: queue.popleft(prvek)
#
# Definici tridy Graph nijak nemodifikujte, ani nepridavejte zadne atributy.
# Zamerne se v teto uloze budete muset obejit bez pomocnych poli ve tride
# Graph; budete muset pouzit lokalni promenne a pripadne parametry v rekurzi.
#
# Nepouzivejte globalni promenne. I kdyz je mozne, ze vyhodnocovaci sluzba
# neodhali vsechna pouziti globalnich promennych, u implementacnich testu
# vas pouzivani globalnich promennych zbytecne pripravi o body. Ma tedy smysl
# se naucit programovat spravne uz ted.


class Graph:
    """Trida Graph drzi graf reprezentovany matici sousednosti.
    Atributy:
        size: velikost (pocet vrcholu) grafu
        matrix: matice sousednosti
                [u][v] reprezentuje hranu u -> v
    """

    def __init__(self, size):
        self.size = size
        self.matrix = [[False] * size for _ in range(size)]


# Ukol 1.
# Implementujte funkci colourable, ktera zjisti, zda je dany neorientovany graf
# obarvitelny dvema barvami tak, aby kazde dva sousedni vrcholy mely ruznou
# barvu.
#
# Neorientovany graf v nasi reprezentaci znamena, ze
#    graph.matrix[u][v] == graph.matrix[v][u] pro vsechny vrcholy u, v.

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
        row = []
        for j in range(graph.size):
            if graph.matrix[i][j]:
                row.append(j)
        result.append(row)
    return result


def find_free(colors):
    for i in range(len(colors)):
        if colors[i] is None:
            return i
    return None


def colourable(graph):
    """Zjisti, zda je zadany neorientovany graf obarvitelny dvema barvami.
    Vstup:
        graph - neorientovany graf typu Graph
    Vystup:
        True, pokud je graf obarvitelny dvema barvami
        False, jinak
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(n), kde n je pocet vrcholu grafu
    """

    # TODO
    succ_list = convert_to_list(graph)
    queue = deque()
    colors = [None] * graph.size
    start = find_free(colors)
    while start is not None:
        queue.append(start)
        colors[start] = True
        while queue:
            node = queue.popleft()
            for i in range(len(succ_list[node])):
                neighbor = succ_list[node][i]
                if colors[neighbor] is None:
                    colors[neighbor] = not colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        start = find_free(colors)
    return True   


# Ukol 2.
# Implementujte funkci compute_dependencies, ktera pro zadany orientovany graf
# spocita topologicke usporadani vrcholu, tj. ocislovani vrcholu takove, ze
# kazda hrana vede z vrcholu s nizsim cislem do vrcholu s vyssim cislem.
#
# Vystupem je pole zadavajici topologicke usporadani (ocislovani vrcholu),
# kde na prvni pozici (tedy s indexem 0) je vrchol nejmensi
# v tomto usporadani, tj. nevede do nej zadna hrana,
# a na posledni pozici vrchol nejvetsi, tj. nevede z nej zadna hrana.
# Pokud topologicke usporadani neexistuje, algoritmus vraci None.
#
# Priklad:
#    mejme graf s vrcholy 0, 1, 2 a hranami 0 -> 1, 2 -> 1, 2 -> 0;
#    vystupem bude pole (Pythonovsky seznam] [2, 0, 1]


def compute_dependencies(graph):
    """Spocita topologicke usporadani vrcholu v grafu.
    Vstup:
        graph - orientovany graf typu Graph
    Vystup:
        pole cisel reprezentujici topologicke usporadani vrcholu
        None, pokud zadne topologicke usporadani neexistuje
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(n), kde n je pocet vrcholu grafu
    """

    # TODO
    succ_list = convert_to_list(graph)
    result = []
    stack = deque()
    discovery_array = [None for _ in range(graph.size)]
    finish_array = [None for _ in range(graph.size)]
    start = 0
    time = 0
    while start is not None:
        time += 1
        stack.append(start)
        discovery_array[start] = time
        while stack:
            time += 1
            node = stack.pop()
            next_node = None
            for successor in succ_list[node]:
                if discovery_array[successor] is None:
                    next_node = successor
                    break
                elif finish_array[successor] is None and discovery_array[successor] < discovery_array[node]:
                    return None
            if next_node is None:
                finish_array[node] = time
                result.append(node)
            else:
                stack.append(node)
                stack.append(next_node)
                discovery_array[next_node] = time
        start = None
        for node in range(graph.size):
            if discovery_array[node] is None:
                start = node
                break
    return list(reversed(result))


graph1 = Graph(4)

graph1.matrix[0][0] = False
graph1.matrix[0][1] = True
graph1.matrix[0][2] = False
graph1.matrix[0][3] = False

graph1.matrix[1][0] = False
graph1.matrix[1][1] = False
graph1.matrix[1][2] = False
graph1.matrix[1][3] = False

graph1.matrix[2][0] = False
graph1.matrix[2][1] = True
graph1.matrix[2][2] = False
graph1.matrix[2][3] = False

graph1.matrix[3][0] = False
graph1.matrix[3][1] = True
graph1.matrix[3][2] = False
graph1.matrix[3][3] = False


graph2 = Graph(2)

graph2.matrix[0][0] = False
graph2.matrix[0][1] = True
graph2.matrix[1][0] = False
graph2.matrix[1][1] = False


graph3 = Graph(1)

graph3.matrix[0][0] = False


graph4 = Graph(3)

graph4.matrix[0][0] = False
graph4.matrix[0][1] = True
graph4.matrix[0][2] = True

graph4.matrix[1][0] = False
graph4.matrix[1][1] = False
graph4.matrix[1][2] = False

graph4.matrix[2][0] = False
graph4.matrix[2][1] = True
graph4.matrix[2][2] = False


graph5 = Graph(4)

graph5.matrix[0][0] = False
graph5.matrix[0][1] = True
graph5.matrix[0][2] = True
graph5.matrix[0][3] = False

graph5.matrix[1][0] = True
graph5.matrix[1][1] = False
graph5.matrix[1][2] = True
graph5.matrix[1][3] = True

graph5.matrix[2][0] = True
graph5.matrix[2][1] = True
graph5.matrix[2][2] = False
graph5.matrix[2][3] = True

graph5.matrix[3][0] = False
graph5.matrix[3][1] = True
graph5.matrix[3][2] = True
graph5.matrix[3][3] = False


print("--------colourable-----------")
print(convert_to_list(graph1))
print(colourable(graph1))
print(convert_to_list(graph2))
print(colourable(graph2))
print(convert_to_list(graph3))
print(colourable(graph3))
print(convert_to_list(graph4))
print(colourable(graph4))
print(convert_to_list(graph5))
print(colourable(graph5))

print("--------topological order-----------")
print(compute_dependencies(graph1))
print(compute_dependencies(graph2))
print(compute_dependencies(graph3))
print(compute_dependencies(graph4))
print(compute_dependencies(graph5))
