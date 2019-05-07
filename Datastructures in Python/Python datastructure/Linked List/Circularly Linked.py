class CircularLinkedList:
    """
    Goal: 想实现的是下面这个数据结构

    假设我们依次进行以下操作:
    add(10)
    add(20)
    add(30)
    add(15)
    add(5)
    会得到以下数据结构

    10 -> 20 -> 30 -> 15 -> 5(cur) -> (10)
    其中:
    1. cur是 节点标记, 方便我们进行查找和删除操作
    2. 第二个10在这里指的是 data 为5 的节点又指向了链表的开头 data为10的节点. 从而
    形成闭合环形链表
    """
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        """
        只使用一个field: cur 来标记现在所在位置
        """
        self.size = 0
        self.cur = None

    def __len(self):
        return self.size

    def add(self, item):
        """
        Goal: 向环形链表中添加 节点
        Description:
        添加new_node时, 链表可以分为以下几种情况:
            1. 链表为空时
            1.1 这个节点就是 cur
            1.2 new_node指向 None
            e.g. :  add(10)
            10(cur) -> None

            2. 链表只有一个node, 添加new_node,使得这两个节点开始形成环状
            2.1 cur标记节点 指向new_node
            2.2 new_node指向cur标记节点 (原来是指向None)
            2.3 cur标记 重新指向new_node (为了统一三种情况的行为: cur永远是
                                        new_node)
            e.g.:
            add(20)
            10 -> 20(cur) -> (10)

            3. 链表有两个以上的节点,这些节点本身就形成环状. 所要做的就是在环状结构上
            再添加一个new_node. 规定: 添加成为cur节点的下一节点,而原来cur节点的下个
            节点 成为 new_node 的下一个节点
            3.1 cur标记节点指向new_node
            3.2 new_node 指向 原来cur标记节点指向的 下个节点
            3.3 cur 现在标记 new_node
            e.g.:
            add(30)
            10 -> 20 -> 30(cur) -> (10)

        """
        new_node = self.Node(item)
        if self.size == 0:
            self.cur = new_node
            new_node.next = None
        elif self.size == 1:
            self.cur.next = new_node
            new_node.next = self.cur
            self.cur = new_node
        else:
            temp = self.cur.next
            self.cur.next = new_node
            new_node.next = temp
            self.cur = new_node

        self.size += 1

    def find(self, item):
        """
        Goal: 在链表中寻找有着对应值item的 第一个找到的 节点. 返回这个节点的索引.
        如果没有发现, 则报告 Find failed.

        Description:
        1. 如果链表为空, 返回 "Find failed: The linked list is empty."
        2. 链表不为空, 从cur标记节点开始寻找, 即 以cur节点的索引为0, 直至
          cur节点的 上一个节点. 寻找范围为 range(self.size).

          2.1 为了方便remove()操作, 在寻找时,要标记节点的上一个节点previous.
            当然,如果链表中, 只有一个节点,那么就无法标记,
            可以设previous的初始为None.
        """
        if self.size == 0:
            return "Find failed: The linked list is empty."
        else:
            previous = self.find_preivous()
            f = self.cur
            for i in range(self.size):
                if not f.data == item:
                    previous = f
                    f = f.next
                else:
                    return (i, previous)

    def find_preivous(self):
        """
        为了找到cur标记节点的上一个节点
        """
        start = self.cur
        for _ in range(self.size-1):
            start = start.next
        preivous = start
        return preivous

    def remove(self, item):
        """
        Goal: 移除链表中对应值的节点
        Descrition:
            1. 如果链表中为空没有节点, 返回"Remove failed: The linked list is
            empty"

            2. 如果链表中不为空, 且找到了对应节点:

            一般情况下所需的操作:
            假设找到了节点 x, x的上一个指向x的节点为 a, x指向的下一个节点为b,则:
            a.next = b
            x.next = None
            如果x是 cur标记节点, 那么 cur = a
            以上操作要保证: a, b 都是实际节点,也就是说 上述操作至少需要链表中有
            三个节点.

            如果链表中只有两个节点,所需的操作:
            a.next = None
            x.next = None
            如果 x是 cur标记节点, 那么 cur = a

            如果链表中只有一节点,所需的操作:
            cur = None
        """
        if self.size == 0:
            return "Remove failed: The linked list is empty."
        elif self.size == 1 and self.cur.data == item:
            self.cur = None
            return None
        elif self.size == 2:
            if self.cur.data == item:
                previous_node = self.cur.next
                self.cur.next = None
            previous_node.next = None
            self.cur = previous_node
            return None
        elif self.size >= 3:
            previous = self.find_preivous()
            start = self.cur
            for i in range(self.size - 1):
                if not start.data == item:
                    previous = start
                    start = start.next
                else:
                    previous.next = start.next
                    start.next = None
                    if i == 0:
                        self.cur = previous
                    return None
        return "Remove failed: The linked list has no such item"


if __name__ == "__main__":
    L = CircularLinkedList()
    L.add(10)       # 10(cur) -> None
    L.add(20)       # 10 -> 20(cur) -> (10)
    L.add(30)       # 10 -> 20 -> 30(cur) -> (10)
    L.add(15)       # 10 -> 20 -> 30 -> 15(cur) -> (10)
    # find()操作按以下所示顺序进行 (使用[]符号作为标记)
    # 10[1] -> 20[2] -> 30[3] -> 15(cur)[0] -> (10[1])
    # print(L.find(15))   # return (0, None)
    # print(L.find(10))   # return (0, Node对象)
    L.add(100)      # 10 -> 20 -> 30 -> 15 -> 100(cur) ->(10)
    print(L.find(10))     # return (1, 节点对象)
    print(L.remove(10))   # return None  20 -> 30 -> 15 -> 100(cur) ->(20)
    print(L.find(100))    # return (0, 节点对象)
