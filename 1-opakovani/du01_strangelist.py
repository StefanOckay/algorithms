#!/usr/bin/env python3


# IB002 Domaci uloha 1.
#
# Vasi ulohou v tomto priklade je modifikovat jiz existujici strukturu
# obousmerne zretezeneho linearniho seznamu.
#
# Obousmerne zretezeny seznam ma atribut first, ktery ukazuje na zacatek
# seznamu, a atribut last, ktery ukazuje na konec seznamu.
#
# Kazdy uzel v seznamu ma tri atributy (value, next a prev). Vlastni seznam
# s hodnotami a, b, c, d, e, f vypada bezne takto (v nakresu vynechavame
# atribut first ukazujici na a a atribut last ukazujici na f):
#       ___   ___   ___   ___   ___
#      /   \ /   \ /   \ /   \ /   \
#     a <-- b <-- c <-- d <-- e <-- f
#
# kde obloucky nad pismeny reprezentuji dopredne sipky (napr. a --> b),
# tedy atributy next.
#
# Nas modifikovany StrangeList pouziva pro reprezentaci stejne promenne,
# pouze atributy ukazuji jinam. Atributy next budou ukazovat ob jeden
# uzel, atributy prev zustanou zachovany. Po prevedeni predchoziho
# seznamu na StrangeList vznikne takovyto seznam (opet vynechavame
# atributy first a last):
#       _________   _________
#      /         \ /         \
#     a <-- b <-- c <-- d <-- e <-- f
#            \_________/ \_________/
#
# StrangeList take obsahuje atribut first, ktery ukazuje na jeho zacatek,
# a atribut last, ktery ukazuje na jeho konec, v tomto pripade:
# first - a, last - f.


# Ukol 1.
# Definujte datovou strukturu StrangeList.
# Muzete se inspirovat definici LinkedList ze zakladniho domaciho ukolu.
# Zakladni metody ci funkce pro praci s LinkedList (jako treba insert) neni
# nutne implementovat, ale mohou se Vam hodit pri tvorbe vlastnich testu.

# TODO
class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

        
class StrangeList:
    def __init__(self):
        self.first = None
        self.last = None
        

# Ukol 2.
# Implementujte funkci list_to_strange_list, ktera z obousmerne
# zretezeneho seznamu vytvori nas StrangeList, tj. upravi atributy next.
# Reprezentaci obousmerne zretezeneho seznamu muzete prevzit ze
# zakladniho domaciho ukolu.

def list_to_strange_list(linkedList):
    """
    vstup: 'linkedList' korektni seznam typu LinkedList
    vystup: stejny seznam s upravenymi atributy next, aby to byl koretni
            StrangeList
    casova slozitost: O(n), kde 'n' je pocet prvku seznamu 'linkedList'
    """
    # TODO
    if linkedList.last is not None:
        cur_node = linkedList.first
        while cur_node.next is not None:
            tmp = cur_node.next
            cur_node.next = cur_node.next.next
            cur_node = tmp
    return linkedList


# Ukol 3.
# Implementujte funkci check_strange_list, ktera zkontroluje, ze atributy
# first a last jsou nastaveny spravne, tj. nejsou to vnitrni uzly seznamu.
# Muzete predpokladat, ze jsou None nebo nejake uzly seznamu s korektne
# nastavenymi atributy next a prev dle pravidel StrangeList seznamu.

def check_strange_list(strangeList):
    """
    vstup: 'strangeList' typu StrangeList s korektnimi atributy next a prev
    vystup: True, pokud jsou v 'strangeList' atributy first a last nastaveny
            korektne
            False, jinak
    casova slozitost: O(1)
    """
    # TODO
    if strangeList.first is None and strangeList.last is None:
        return True
    if strangeList.first is strangeList.last:
        return strangeList.first.prev is None and strangeList.last.next is None
    return strangeList.first.prev is None and strangeList.last.next is None and strangeList.last.prev.next is None
