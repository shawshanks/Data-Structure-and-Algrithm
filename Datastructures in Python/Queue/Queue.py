"""
Descrition:
    Queue is a kind of abstract data type in which the first element must be
    access and delete first. This is what is said FIFO (first-in, first-out).

    And the newly added element must be add at the back of the sequence.

class Diagram:

Behavior:
    Q.enqueue(e): Add an element in the queue. The newly added element must be
                at the back of Q.
    Q.dequeue(e): Remove the first element and return it.

optional Behavior:
    len(Q): return the number of elements in Q

"""


class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, e):
        self._data.insert(0, e)

    def dequeue(self):
        if len(self._data) > 0:
            return self._data.pop(0)
        else:
            print("No element: the Queue is empty")


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
