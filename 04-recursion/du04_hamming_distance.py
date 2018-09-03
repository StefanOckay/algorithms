#!/usr/bin/env python3

# Povolene knihovny: copy, math
# Import jakekoli jine knihovny neprojde vyhodnocovaci sluzbou.

# IB002 Domaci uloha 4.
#
# Hammingovu vzdalenost dvou stejne dlouhych binarnich retezcu
# definujeme jako pocet bitu, ve kterych se retezce lisi.
#
# Vasim ukolem je implementovat funkci hamming_distance,
# ktera pro binarni retezec 'b' a nezaporne cele cislo 'k' vrati vsechny
# binarni retezce, jejichz Hammingova vzdalenost od 'b' bude prave 'k'.
#
# Priklady chovani:
# hamming_distance('100', 0) vrati vystup: ['100']
# hamming_distance('0001', 2) vrati vystup:
#         ['1101', '1011', '1000', '0111', '0100', '0010']


def hamming_distance_array(b, k, b_from, lenb, result):
    
    if k == 0:
        s = ''.join(b)
        result.append(s)
    for i in range(b_from, lenb):
        if b[i] is '1':
            b[i] = '0'
        else:
            b[i] = '1'
        hamming_distance_array(b, k - 1, i + 1, lenb, result)
        if b[i] is '1':
            b[i] = '0'
        else:
            b[i] = '1'
            


def hamming_distance(b, k):
    """
    vstup: 'b' binarni retezec, 'k' nezaporne cele cislo
    vystup: pole vsech binarnich retezcu se vzdalenosti 'k' od 'b'
    casova slozitost: polynomialni vzhledem k delce binarniho retezce 'b'
        ( To znamena, ze pocet operaci je v O(n^j), kde 'n' je delka binarniho
          retezce 'b' a 'j' je nejake fixni cislo. Tedy pro slozitostni odhad
          'k' povazujeme za fixni. Vsimnete si, ze pokud budete generovat
          vsechny binarni retezce stejne delky jako 'b' a nasledne merit
          Hammingovu vzdalenost, tak se nevejdete do pozadovane slozitosti.
          Doporucejeme se zamyslet nad rekurzivnim pristupem. )
    """
    # TODO
    result = []
    lenb = len(b)
    b_mutable = [b[i] for i in range(lenb)]
    hamming_distance_array(b_mutable, k, 0, lenb, result)
    return result


print(hamming_distance('11111', 2))
