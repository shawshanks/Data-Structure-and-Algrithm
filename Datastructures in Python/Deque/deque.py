"""
descrition:
    Deque is a kind of abstract type in which an element can be added and
    removed from either first(head) or rear(tail).

class diagram:

Fields:
    _data : use a existing data structure to implement the behaviors of deque.

Behaviors:
    add_first(e): Add a element to the front of deque.
    add_last(e): Add a element to the rear of deque.
    delete_first(e): remove and return the first element of the deque. If the
                deque is empty, prompt the deque is empty
    delete_last(e): remove and return the last element of the deque. If the
                deque is empty, prompt the deque is empty
    len(deque): return the length of deque.
"""


class Deque:
    def __init__(self):
        self._data = []   # use list as fundamental data structure

    def __len__(self):
        return len(self._data)

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if len(self._data) > 0:
            return self._data.pop(0)
        else:
            print("Empty deque")

    def delete_last(self):
        if len(self._data) > 0:
            return self._data.pop()
        else:
            print("Empty deque")


if __name__ == '__main__':
    D = Deque()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    print(D.delete_last())
    print(len(D))
    print(D.delete_last())
    print(D.delete_last())
    print(D.delete_first())
