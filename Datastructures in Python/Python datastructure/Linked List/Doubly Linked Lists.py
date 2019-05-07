class DoublyLinkedList:
    """
    使用哨兵的双端链表
    """
    class Node:
        def __init__(self, data=None, pre=None, next=None):
            self.data = data
            self.pre = pre
            self.next = next

    def __init__(self, head=None, tail=None):
        self.size = 0
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.size

    def add(self, item):
        new_node = self.Node(item)

        new_node.next = self.head.next
        self.head.next.prev = new_node

        self.head.next = new_node
        new_node.prev = self.head

    def remove(self, item):
        start = self.head.next
        for i in range(len(self.size)):
            if not start.data == item:
                start = start.next
            else:
                start.prev.next = start.next
                start.next.prev = start.prev
                return "Remove Success!"
        return "Remove failed: There is no such item"






