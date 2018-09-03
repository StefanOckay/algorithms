#!/usr/bin/env python3
import time
import sys
import math


sys.setrecursionlimit(6000)  # nastavi maximalni hloubku rekurze na 6000

# Vasim ukolem bude naimplementovat ruzne verze algoritmu pro vypocet
# mocniny a pro vypocet fibonacciho cisel. Testy obsahuji mereni
# rychlosti, takze si pro ruzne casove tridy muzete udelat predstavu,
# jak dlouho bezi.
#
# Doba behu neni deterministicka - jednou muze vypocet probehnout
# rychle, podruhe pomalu. Proto jsou testy rychlosti nekolikrat
# opakovany a namereny cas neni dobou behu jednoho vypoctu.
# I tak je cas pouze orientacni.


# TODO: dopsat implementaci
def power_iterative(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci iterativniho algoritmu
    v O(exp). Staci se omezit na prirozene hodnoty exp.
    """
    # TODO
    result = 1
    for i in range(exp):
        result *= base
    return result

# TODO: dopsat implementaci
def power_bin_iterative(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci iterativniho algoritmu
    v O(log(exp)). Staci se omezit na prirozene hodnoty exp.

    Vyuziva predpokladu, ze n lze rozlozit na soucet mocnin dvojky,
    takze a^n lze rozlozit na soucin ruznych a na mocninu 2,
    tedy a^(2^k). a^(2^k) = ((((a^2)^2)^2)...^2), kde je k pocet dvojek.
    """
    # TODO
    res = 1
    if (exp < 0):
        exp = -exp
        base = 1 / base
    while exp > 0:
        if (exp % 2 == 1):
            res = res * base
        base = base * base
        exp = exp // 2
    return res


# TODO: dopsat implementaci
def power_recursive(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci rekurzivniho algoritmu
    v O(exp). Staci se omezit na prirozene hodnoty exp.
    """
    # TODO
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)


# TODO: dopsat implementaci
def power_bin_recursive(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci rekurzivniho algoritmu
    v O(log(exp)). Staci se omezit na prirozene hodnoty exp.
    """
    # TODO    
    if (exp < 0):
        exp = -exp
        base = 1 / base
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return base * power_bin_recursive(base, exp // 2) * power_bin_recursive(base, exp // 2)
    else:
        return power_bin_recursive(base, exp // 2) * power_bin_recursive(base, exp // 2)


# TODO: dopsat implementaci
def power_real_numbers(base, exp):
    """Funkce vypocita hodnotu base^exp pomoci libovolneho algoritmu.
    Funkce musi fungovat na realne hodnoty exp. Muzete si dopsat pomocne
    funkce. Na interval exponentu (0, 1) muzete pouzit operator **,
    pokud vsak zkusite resit i tento interval, verte, ze se hodne
    priucite, je to narocne.
    """
    # TODO
    if (exp < 0):
        exp = -exp
        base = 1 / base
    expn = int(exp)
    res =  power_bin_iterative(base, expn)
    expdec = exp - expn
    res *= base**expdec
    return res


# TODO: dopsat implementaci
def fib_recursive(number):
    """Funkce vypocita number-te finonacciho cislo pomoci
    exponencialniho rekurzivniho algoritmu.
    0. fibonacciho cislo je 0, 1. je 1
    """
    # TODO
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib_recursive(number - 1) + fib_recursive(number - 2)


# TODO: dopsat implementaci
def fib_iter(number):
    """Funkce vypocita number-te finonacciho cislo pomoci linearniho
    iterativniho algoritmu.
    0. fibonacciho cislo je 0, 1. je 1
    """
    # TODO
    if number == 0:
        return 0
    prevprev = 0
    prev = 1
    cur = 1
    for i in range(number - 1):
        cur = prev + prevprev
        prevprev = prev
        prev = cur
    return cur
        


# Testy implementace
def test_power():
    print("0. Cas vestaveneho mocneni v Pythonu: ", end="")
    start = time.clock()
    counter1 = 0
    for i in range(1, 3000):
        counter1 += 13 ** i
    end = time.clock()
    print("{} s.".format(end - start))

    print("1. Cas iterativniho mocneni v O(exp): ", end="")
    start = time.clock()
    counter2 = 0
    for i in range(1, 3000):
        counter2 += power_iterative(13, i)
    end = time.clock()
    print("{} s.".format(end - start))
    if counter1 != counter2:
        print("Vase funkce power_iterative nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_iterative je", power_iterative(7, i))
    else:
        print("Vysledek je OK.")

    print("\n2. Cas iterativniho mocneni v O(log(exp)): ", end="")
    start = time.clock()
    counter3 = 0
    for i in range(1, 3000):
        counter3 += power_bin_iterative(13, i)
    end = time.clock()
    print("{} s.".format(end - start))
    if counter1 != counter3:
        print("Vase funkce power_bin_iterative nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_bin_iterative je",
                  power_bin_iterative(7, i))
    else:
        print("Vysledek je OK.")

    print("\n3. Cas rekurzivniho mocneni v O(exp): ", end="")
    start = time.clock()
    counter4 = 0
    for i in range(1, 3000):
        counter4 += power_recursive(13, i)
    end = time.clock()
    print("{} s.".format(end - start))
    if counter1 != counter4:
        print("Vase funkce power_recursive nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_recursive je", power_recursive(7, i))
    else:
        print("Vysledek je OK.")

    print("\n4. Cas rekurzivniho mocneni v O(log(exp)): ", end="")
    start = time.clock()
    counter5 = 0
    for i in range(1, 3000):
        counter5 += power_bin_recursive(13, i)
    end = time.clock()
    print("{} s.".format(end - start))
    if counter1 != counter5:
        print("Vase funkce power_bin_recursive nedava stejny vystup jako **.")
        for i in range(10):
            print("7 ^ {} = {},".format(i, 7 ** i))
            print("vas vystup power_bin_recursive je",
                  power_bin_recursive(7, i))
    else:
        print("Vysledek je OK.")


def test_extended_power():
    print("\n5. Test power pro realna cisla zakladu (nemeri se cas).")
    ok = True
    for i in range(-10, 10):
        if abs(7.5 ** i - power_real_numbers(7.5, i)) > 0.1 * (7.5 ** i):
            print("vas vystup z power_real_numbers se lisi",
                  "od ** o vice nez 10 %")
            print("7.5 ^ {} = {},".format(i, 7.5 ** i))
            print("vas vystup power_real_numbers je",
                  power_real_numbers(7.5, i))
            ok = False
    if ok:
        print("Vysledek je OK.")

    print("\n6. Test power pro realna cisla ", end="")
    print("(exponentu i zakladu, nemeri se cas).")
    ok = True
    for i in range(-10, 10):
        if (abs(7.5 ** (i + 0.5) - power_real_numbers(7.5, (i + 0.5))) >
                0.1 * (7.5 ** (i + 0.5))):
            print("vas vystup z power_real_numbers se lisi",
                  "od ** o vice nez 10 %")
            print("7.5 ^ {} = {},".format(i + 0.5, 7.5 ** (i + 0.5)))
            print("vas vystup power_real_numbers je",
                  power_real_numbers(7.5, (i + 0.5)))
            ok = False
    if ok:
        print("Vysledek je OK.")


def test_fib():
    print("\n7. Cas vypoctu fibonacciho cisla 35 v O(2^n): ", end="")
    start = time.clock()
    result = fib_recursive(35)
    end = time.clock()
    print("{} s.".format(end - start))
    if result != 9227465:
        print("Vase funkce fib_recursive nepocita spravne.",
              "Nasleduji vysledky do 35:")
        for i in range(35):
            print("fib_recursive({}) = {}".format(i, fib_recursive(i)))
    else:
        print("Vysledek je OK.")

    print("\n8. Cas vypoctu fibonacciho cisla 350000 v O(n): ", end="")
    start = time.clock()
    fib_iter(350000)
    end = time.clock()
    print("{} s.".format(end - start))
    if fib_iter(35) != 9227465:
        print("Vase funkce fib_iter nepocita spravne.",
              "Nasleduji vysledky do 35:")
        for i in range(35):
            print("fib_iter({}) = {}".format(i, fib_iter(i)))
    else:
        print("Vysledek je OK.")


if __name__ == '__main__':
    test_power()
    test_extended_power()
    test_fib()
