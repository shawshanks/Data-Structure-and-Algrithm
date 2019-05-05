"""
Data: 2019.5.4
Author: Yang good man

> 一切的一切,都又回到原点

使用单向链表完成序列的一般操作:
使用方法:                           说明
L = SingleLinkedList_Squence()     初始化一个 单向链表支持的序列
len(L)                             查询 序列长度
L.add(item)                        在序列开头处插入元素, 类似于 list.append(0)
L.append(item)                     在序列结尾处插入元素, 类似于 list.append()
L.search(item)                     查询序列中是否有item,类似于 item in list
L.insert(item, i)                  在索引i处插入item,类似于 list[i]=item
L.index(item)                      返回item第一次在序列中出现的索引
L.index_to_value(i)                查询索引处的值, 类似于 list[i]
L.remove(item)                     移除列表中第一个值为item的元素
"""


class SingleLinkedList_Squence:

    #  --------------------嵌套类Node-----------------------------------------
    # Nesting class 嵌套类作用

    # 1.Nesting one class in the scope of another makes clear that the nested
    # class exists for the support of the outer class.

    # 2. Reduce potential name conflicts

    # 3. For advanced form of inheritance. A subclass of outer class could
    # overrides the nested class.
    class Node:
        """
        Node model:
        None <-  10  <-  20  <-  30 <- 40
        """
        def __init__(self, data, next=None):
            """
             一个节点诞生时的样子, 你赋予他一个灵魂(值),而它总是指向None
            """
            self.data = data
            self.next = next
            self.index = None  # 能够变成你熟悉的样子,不好吗
    # ---------------------Nest class Node end --------------------------------

    def __init__(self):
        """
        一个链表诞生时,一切即为None或0
        """
        self._head = None  # head tag
        self._tail = None  # tail tag
        self._size = 0  # 常数时间内实现 len() , 类似于Python list的len()实现

    def __len__(self):
        return self._size

    def add(self, item):
        """
        一切开头难, 第一个node总是特殊的,它既为head,亦为tail.

        而后增加node 最简单最直观的方式:
        1. 将node指向原来链表的head (欢迎加入集体)
        2. 带上head的帽子 (将head指向 此node)

        别忘了你又长大了一岁哦(长度+1)
        """
        new_node = self.Node(item)
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def append(self, item):
        """
        一切开头难, 第一个node总是特殊的,它既为head,亦为tail.

        而后在尾部增加节点,这意味着
        1. 这个节点是 tail, 而tail节点 是指向None的(node.next=None). Node 诞生时
        就满足要求,不必改变.
        2. 要把原来的tail node指向这个 现在这个尾节点
        3. 1和2 完成后,这个node成为了实质上的尾节点. 但是还是要带上tail的帽子,向大家
            宣布此node是tail.

        你又长大了一岁(长度+1)
        """
        new_node = self.Node(item)
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def search(self, item):
        start = self._head
        for _ in range(self._size):
            if start.data == item:
                return True
            start = start.next
            if start is None:
                print("Seach failed: no such item")

    def index(self, item):  # 保持和列表一样的接口 list.index()
        """
        虽然内心是完全不同的(compare to arry-based), 但是表面行为还是要保持一致,不
        然大家会认为你是个怪物 :(

        行为: 给出第一次出现item的索引

        免为其难的做吧~!虽然比较累(遍历)
        """
        start = self._head  # 从头开始搜索
        for i in range(self._size):
            if start.data == item:
                return i
            start = start.next
            if start is None:
                print("Index failed: no such item")

    def index_to_value(self, index):
        """
        模仿 list[i]
        """
        start = self._head
        for _ in range(index):
            start = start.next
        return start.data

    def insert(self, item, index):
        """
        如果不能插入,那这个世界又有什么意思

        行为: 支持在索引处插入node

        说明:
        1. special case:如果是在开头或结尾处插入,那么使用 add()或append()工具.

        2. 在中间插入的情况: 规定,原来索引处的节点向后移动. 即new_node指向原来位置的
         original_node.

        3. 指向 orignial_node 的上个节点 现在要 指向 new_node.

        此外别忘了 链表又长胖了啊! (长度+1)
        """
        new_node = self.Node(item)
        if index == 0:
            self.add(new_node)
        elif index == self._size - 1:
            self.append(new_node)
        else:
            start = self._head
            for i in range(index):
                previous = start     #
                start = start.next

            new_node.next = start
            previous.next = new_node

            self._size += 1

    def remove(self, item):
        start = self._head
        previous = None
        for _ in range(self._size):
            if start.data != item:
                previous = start
                start = start.next
                if start is None:
                    print("Remove faild: no such item")
            else:
                previous.next = start.next
                self._size -= 1
                break

    def delete(self, index):
        """
        行为: 删除索引为index处的node

        说明:
            1. 找到索引处node 和 指向它的 上一个node
            2. 它的上一个节点现在不能指向 这个node了,而是指向这个node的下一个节点
            3. 这个节点 现在指向 None
            4. 别忘了 链表变瘦了 (长度-1)
        """
        start = self._head
        for _ in range(index):
            previous = start
            start = start.next
        previous.next = start.next
        start.next = None

        self._size -= 1

if __name__ == '__main__':
    L = SingleLinkedList_Squence()
    L.add(10)       # 10 -> None
    L.add(20)       # 20 -> 10 -> None
    L.add(30)       # 30 -> 20 -> 10 -> None
    L.add(40)       # 40 -> 30 -> 20 -> 10 -> None
    L.append(5)     # 40 -> 30 -> 20 -> 10 -> 5 -> None
    L.append(4)     # 40 -> 30 -> 20 -> 10 -> 5 -> 4 -> None
    print(len(L))
    print(L._head.data)
    print(L.search(30))
    print(L.index(30))
    print(L.index(4))
    L.remove(10)    # 40 -> 30 -> 20 ->  5 -> 4 -> None
    print(L.search(10))
    print(len(L))
    L.remove(100)
    print(L.search(5))
    L.insert(100, 2)     # 40 -> 30 -> 100 -> 20 ->  5 -> 4 -> None
    print(L.index_to_value(2))  # return 100
    print(L.index_to_value(1))  # return 30
    print(L.index_to_value(3))  # return 20
    L.delete(2)          # 40 -> 30 -> 20 ->  5 -> 4 -> None
    print(L.index_to_value(2))  # return 20








