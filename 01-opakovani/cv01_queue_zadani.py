#!/usr/bin/env python3


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
    new_node = Item()
    new_node.value = value
    new_node.left = None
    if is_empty(queue):
        queue.first = new_node
        queue.last = new_node
    else:
        queue.last.left = new_node
        queue.last = new_node


def dequeue(queue):
    """Metoda dequeue odebere prvni prvek z fronty (queue).
    Vraci hodnotu (value) odebraneho prvku, pokud je fronta prazdna,
    vraci None
    """
    # TODO
    if is_empty(queue):
        return None
    tmp = queue.first
    if queue.last is queue.first:
        queue.last = None
    queue.first = queue.first.left
    tmp.left = None
    return tmp.value


def is_empty(queue):
    """is_empty() vraci True v pripade prazdne fronty, jinak False."""
    # TODO
    return queue.last is None and queue.first is None


# Testy implementace
def test_enqueue_empty():
    print("Test 1. Vkladani do prazdne fronty: ", end="")

    q = Queue()
    enqueue(q, 1)

    if q.first is None or q.last is None:
        print("FAIL")
        return

    if (q.first.value == 1 and q.first.left is None and
            q.last.value == 1 and q.last.left is None):
        print("OK")
    else:
        print("FAIL")


def test_enqueue_nonempty():
    print("Test 2. Vkladani do neprazdne fronty: ", end="")

    q = Queue()
    i = Item()
    i.left = None
    i.value = 1
    q.first = i
    q.last = i

    enqueue(q, 2)

    if q.first is None or q.last is None:
        print("FAIL")
        return
    if q.last.value == 2 and q.first == i and q.first.left.value == 2:
        print("OK")
    else:
        print("FAIL")


def test_dequeue_empty():
    print("Test 3. Odebirani z prazdne fronty: ", end="")

    q = Queue()
    v = dequeue(q)

    if v is not None or q.first is not None or q.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_dequeue_nonempty():
    print("Test 4. Odebirani z neprazdne fronty: ", end="")

    q = Queue()
    i = Item()
    i.value = 1
    i.left = None
    q.first = i
    q.last = i

    v = dequeue(q)

    if v != 1 or q.first is not None or q.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_is_empty_empty():
    print("Test 5. is_empty na prazdne fronte: ", end="")

    q = Queue()

    if is_empty(q):
        print("OK")
    else:
        print("FAIL")


def test_is_empty_nonempty():
    print("Test 6. is_empty na neprazdne fronte: ", end="")

    q = Queue()
    i = Item()
    i.left = None
    i.value = 1
    q.first = i
    q.last = i

    if is_empty(q):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_enqueue_empty()
    test_enqueue_nonempty()
    test_dequeue_empty()
    test_dequeue_nonempty()
    test_is_empty_empty()
    test_is_empty_nonempty()
