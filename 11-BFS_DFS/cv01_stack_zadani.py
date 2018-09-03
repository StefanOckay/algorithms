#!/usr/bin/python3


class Item_Stack:
    """ Trida Item_Stack slouzi pro reprezentaci objektu v zasobniku.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        below   reference na predchazejici prvek v zasobniku
    """
    def __init__(self):
        self.value = None
        self.below = None


class Stack:
    """Trida stack reprezentuje zasobnik.

    Atributy:
        top     reference na vrchni prvek v zasobniku
    """
    def __init__(self):
        self.top = None


def push(stack, value):
    """Metoda push() vlozi na vrchol zasobniku (stack) novy prvek
    s hodnotou (value).
    """
    # TODO
    new = Item_Stack()
    new.value = value
    if isEmpty_Stack(stack):
        new.below = None
    else:
        new.below = stack.top
    stack.top = new

def pop(stack):
    """Metoda pop() odebere vrchni prvek zasobniku. Vraci hodnotu
    (value) odebraneho prvku, pokud je zasobnik prazdny vraci None.
    """
    # TODO
    if isEmpty_Stack(stack):
        return None
    else:
        theNode = stack.top
        stack.top = stack.top.below
        theNode.below = None
        return theNode.value

def isEmpty_Stack(stack):
    """Metoda isEmpty_Stack() vraci True v pripade prazdneho zasobniku,
    jinak False.
    """
    # TODO
    return stack.top is None

# Testy implementace
def test_push_empty():
    print("Test 1. Vkladani do prazdneho zasobniku: ", end="")

    s = Stack()
    push(s, 1)

    if s.top is None:
        print("FAIL")
        return

    if s.top.value is 1 and s.top.below is None:
        print("OK")
    else:
        print("FAIL")


def test_push_nonempty():
    print("Test 2. Vkladani do neprazdneho zasobniku: ", end="")

    s = Stack()
    i = Item_Stack()
    i.below = None
    i.value = 1
    s.top = i

    push(s, 2)

    if s.top is None:
        print("FAIL")
        return
    if s.top.value == 2 and s.top.below == i:
        print("OK")
    else:
        print("FAIL")


def test_pop_empty():
    print("Test 3. Odebirani z prazdneho zasobniku: ", end="")

    s = Stack()
    v = pop(s)

    if v is not None or s.top is not None:
        print("FAIL")
    else:
        print("OK")


def test_pop_nonempty():
    print("Test 4. Odebirani z neprazdneho zasobniku: ", end="")
    s = Stack()
    i = Item_Stack()
    i.value = 1
    i.below = None
    s.top = i

    v = pop(s)

    if v is not 1 or s.top is not None:
        print("FAIL")
    else:
        print("OK")


def test_isEmpty_Stack_empty():
    print("Test 5. isEmpty_Stack na prazdnem zasobniku: ", end="")

    s = Stack()

    if isEmpty_Stack(s):
        print("OK")
    else:
        print("FAIL")


def test_isEmpty_Stack_nonempty():
    print("Test 6. isEmpty_Stack na neprazdnem zasobniku: ", end="")

    s = Stack()
    i = Item_Stack()
    i.below = None
    i.value = 1
    s.top = i

    if isEmpty_Stack(s):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_push_empty()
    test_push_nonempty()
    test_pop_empty()
    test_pop_nonempty()
    test_isEmpty_Stack_empty()
    test_isEmpty_Stack_nonempty()
