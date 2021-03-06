#!/usr/bin/env python3
import random
from collections import deque


# Vasim ukolem v teto implementacni uloze je naprogramovat zakladni
# radici algoritmy. Formulace problemu neni vzdy stejna jako je ve
# sbirce, musite splnit zadani v komentari nad funkci.
#
# Povinne jsou pro vas radici algoritmy InsertSort, MergeSort, QuickSort
# a CountingSort. Zbyle algoritmy presto doporucujeme naimplementovat.


def swap(array, i, j):
    """Pomocna funkce swap pro vas, bere argumenty pole 'array', ve kterem
    prohodi prvky na pozicich indexu 'i' a 'j'.
    """
    array[i], array[j] = array[j], array[i]


# TODO: dopsat tuto funkci
def insert_sort(array):
    """Razeni vkladanim. V kazdem pruchodu se nasledujici prvek posouva
    v poli 'array' tak dlouho, dokud nenarazi na mensi prvek, nebo na zacatek.
    Velikost vstupniho pole ziskate pomoci 'len(array)'.
    """
    # TODO
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1


def partition(array, p, r):
    pivot = array[r]
    i = p - 1
    for j in range(p, r + 1):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    return i


def hoarepartition(array, p, r):
    if p <= r:
        i = p
        j = r
        pivot = array[r]
        while True:
            while pivot > array[i]:
                i += 1
            while pivot < array[j]:
                j -= 1
            if array[i] == array[j]:
                i += 1
            if i < j:
                swap(array, i, j)
            else:
                return j


def quick_sort_in_place_recursive(array, i, j):
    if i < j:
        mid = hoarepartition(array, i, j)
        quick_sort_in_place_recursive(array, i, mid - 1)
        quick_sort_in_place_recursive(array, mid + 1, j)


def quick_sort_in_place_iterative(array, i, j):
    stack = deque()
    stack.append([i, j])
    while stack:
        i, j = stack.pop()
        mid = hoarepartition(array, i, j)
        if mid + 1 < j:
            stack.append([mid + 1, j])
        if i < mid - 1:
            stack.append([i, mid - 1])


# TODO: dopsat tuto funkci
def quick_sort_in_place(array, i, j):
    """Razeni rozdelovanim (QuickSort). Zadane pole 'array' v rozsahu
    indexu 'i' a 'j' rekurzivne seradte bez pouziti pomocneho pole.
    Jako pivot se voli posledni prvek zadaneho rozsahu.
    """
    # TODO
    quick_sort_in_place_iterative(array, i, j)


# TODO: dopsat tuto funkci
def merge(array, aux, left, mid, right):
    """Slevani pro razeni spojovanim (MergeSort). Zadane pole 'array'
    obsahuje 2 usporadane posloupnosti v intervalech od 'left' po 'mid'
    a od 'mid'+1 po 'right'. K spojeni pouzijte pomocne pole 'aux'.
    Vysledek ulozte v poli 'array'.
    """
    # TODO
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if array[i] > array[j]:
            aux[k] = array[j]
            j += 1
        else:
            aux[k] = array[i]
            i += 1
        k += 1
    if i == mid + 1:
        while j <= right:
            aux[k] = array[j]
            j += 1
            k += 1
    if j == right + 1:        
        while i <= mid:
            aux[k] = array[i]
            i += 1
            k += 1
    for k in range(right - left + 1):
        array[k + left] = aux[k]    


# TODO: dopsat tuto funkci
def merge_sort(array, aux, left, right):
    """Razeni spojovanim (MergeSort). Seradte zadane pole 'array'
    v intervalu od indexu 'left' po index 'right'.
    Pouzijte pomocnou funkci 'merge' a pomocne pole 'aux'. Vysledek
    ulozte v poli 'array'.
    """
    # TODO
    if left < right:
        merge_sort(array, aux, left, (left + right) // 2)
        merge_sort(array, aux, (left + right) // 2 + 1, right)
        merge(array, aux, left, (left + right) // 2, right)


# TODO: dopsat tuto funkci
def counting_sort(array, low, high):
    """Razeni pocitanim (CountingSort). Seradte zadane pole 'array'
    pricemz o poli vite, ze se v nem nachazeji pouze hodnoty v intervalu
    od 'low' po 'high' (vcetne okraju intervalu). Vratte serazene pole.
    """
    # TODO
    high_adj = high - low
    counts = [0 for i in range(high_adj + 1)]
    for i in range(len(array)):
        counts[array[i] - low] += 1
    k = 0
    i = 0
    while i < len(counts):
        for j in range(counts[i]):
            array[k] = i + low
            k += 1
        i += 1
    return array


# Nasledujici radici algoritmy nejsou povinne, presto je doporucujeme
# naimplementovat jako cviceni. Nejsou to nejtezsi radici algoritmy,
# takze je mozna vhodne je v ramci treninku implementovat drive nez
# zbyle optimalni radici algoritmy.


# TODO: dopsat tuto funkci
def min_index(array, i, j):
    """Pomocna funkce pro razeni vyberem. Vrati index nejmensiho prvku
    v poli 'array' mezi 'i' a 'j'-1.
    """
    # TODO
    len_ij = j - i + 1
    min_index = i
    for k in range(i + 1, j + 1):
        if array[k] < array[min_index]:
            min_index = k
    return min_index


# TODO: dopsat tuto funkci
def select_sort(array):
    """Seradte pole 'array' pomoci razeni vyberem."""
    # TODO
    min_i = 0
    lena = len(array)
    for i in range(lena - 1):
        min_i = min_index(array, i, lena - 1)
        swap(array, i, min_i)


# Dale nasleduji kody potrebne k testum, needitujte je.

ELEMENT_COUNT = 10
MAX_ELEMENT = 50


def new_random_array(size, max_element=MAX_ELEMENT):
    """Slouzi pro generovani noveho pole delky size."""
    return [random.randint(1, max_element) for _ in range(size)]


def is_correct_result(in_array, out_array):
    return sorted(in_array) == out_array


def run_quick_sort(array):
    quick_sort_in_place(array, 0, len(array) - 1)


def run_merge_sort(array):
    aux = [0 for i in range(len(array))]
    merge_sort(array, aux, 0, len(array) - 1)


def test_sort(sort):
    print("Test 1.: jednoprvkove pole [1]: ")
    array1 = [1]
    orig = array1[:]
    sort(array1)

    if is_correct_result(orig, array1):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1] a bylo serazeno,")
        print("po volani sortu je vystup: {}".format(array1[0]))

    print("Test 2.: dvouprvkove pole [1, 2]: ")
    array2 = [1, 2]
    orig = array2[:]
    sort(array2)

    if is_correct_result(orig, array2):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2] a bylo serazeno,")
        print("po volani sortu je vystup: {}".format(array2))

    print("Test 3.: dvouprvkove pole [2, 1]: ")
    array3 = [2, 1]
    orig = array3[:]
    sort(array3)

    if is_correct_result(orig, array3):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [2, 1],")
        print("po volani sortu je vystup: {}".format(array3))

    print("Test 4.: serazene pole 10 prvku [1..10]: ")
    array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    orig = array4[:]
    sort(array4)

    if is_correct_result(orig, array4):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2..10],")
        print(" po volani sortu je vystup: {}".format(array4))

    print("Test 5.: neserazene pole: ")
    array5 = new_random_array(ELEMENT_COUNT)
    print("Puvodni pole: {}".format(array5))
    orig = array5[:]
    sort(array5)

    if is_correct_result(orig, array5):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: {}".format(array5))


def test_insert_sort():
    print("Testy na InsertSort:")
    test_sort(insert_sort)


def test_quick_sort():
    print("\nTesty na QuickSort:\n")
    test_sort(run_quick_sort)


def test_merge():
    print("\nTesty na Merge z MergeSortu:\n")
    aux = [0 for i in range(ELEMENT_COUNT)]

    print("Test 1.: Merge 2 jednoprvkovych stejnych poli [1] a [1]:")
    array1 = [1, 1]
    merge(array1, aux, 0, 0, 1)

    if array1[0] == 1 and array1[0] == 1:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 1],")
        print("po volani Merge je vystup: {}".format(array1))

    print("Test 2.: Merge 2 jednoprvkovych stejnych poli [1] a [2]:")
    array2 = [1, 2]
    merge(array2, aux, 0, 0, 1)

    if array2[0] == 1 and array2[1] == 2:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2],")
        print("po volani Merge je vystup: {}".format(array2))

    print("Test 3.: dvouprvkove pole [2, 1]: ")
    array3 = [2, 1]
    merge(array3, aux, 0, 0, 1)

    if array3[0] == 1 and array3[1] == 2:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [2, 1], vysledek mel byt [1, 2],")
        print("po volani Merge je vystup: {}".format(array3))

    print("Test 4.: desetiprvkove pole [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]:")
    array4 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    orig = array4[:]
    merge(array4, aux, 0, 4, 9)

    if is_correct_result(orig, array4):
        print("OK")
    else:
        print("NOK, vysledek mel byt [1..10],")
        print("po volani Merge je vystup: {}".format(array4))

    print("Test 5.: desetiprvkove pole [1, 1, 2, 2, 3, 1, 1, 2, 3, 3]:")
    array5 = [1, 1, 2, 2, 3, 1, 1, 2, 3, 3]
    orig = array5[:]
    merge(array5, aux, 0, 4, 9)

    if is_correct_result(orig, array5):
        print("OK")
    else:
        print("NOK, vysledek mel byt [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],")
        print("po volani Merge je vystup: {}".format(array5))


def test_merge_sort():
    print("\nTesty na MergeSort:")
    test_sort(run_merge_sort)


def run_counting_sort(array):
    array[:] = counting_sort(array, 0, MAX_ELEMENT)


def test_counting_sort():
    print("\nTesty na CountingSort:")
    test_sort(run_counting_sort)

    print("Test 6.: neserazene pole malo hodnot:")
    array = new_random_array(ELEMENT_COUNT, ELEMENT_COUNT // 3)
    orig = array[:]
    print("Puvodni pole: " + str(array))
    array = counting_sort(array, 0, ELEMENT_COUNT // 3)

    if is_correct_result(orig, array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))

    print("Test 7.: neserazene pole malo hodnot posunute:")
    array = new_random_array(ELEMENT_COUNT, ELEMENT_COUNT // 3)
    for i in range(ELEMENT_COUNT):
        array[i] += 20

    orig = array[:]
    print("Puvodni pole: {}".format(array))
    array = counting_sort(array, 20, 20 + ELEMENT_COUNT // 3)

    if is_correct_result(orig, array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))


def test_select_sort():
    print("\nTesty na SelectSort:")
    test_sort(select_sort)


def run_bucket_sort(array):
    bucket_sort(array, MAX_ELEMENT)


if __name__ == '__main__':
    test_insert_sort()
    test_quick_sort()
    test_merge()
    test_merge_sort()
    test_counting_sort()
    # BONUS
    test_select_sort()
