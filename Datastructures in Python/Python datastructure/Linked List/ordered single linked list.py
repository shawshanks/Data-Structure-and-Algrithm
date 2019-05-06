"""
Date: 2019.05.06
Author: Yang
Using single linked list to implement Ordered sequence.

The Ordered list ADT support such operations:

操作(方法)                           说明
L =OrderedList()                      创建 并 返回 新的有序列表
len(L)                             查询 序列长度
L.add(item)                        向链表中插入 节点,根据item大小进行排列
L.search(item)                     查询序列中是否有item,类似于 item in list
L.index(item)                      返回item第一次在序列中出现的索引
L.index_to_value(i)                查询索引处的值, 类似于 list[i]
L.remove(item)                     移除列表中第一个值为item的元素
"""


class OrderedList:
    """
    链表特征:
    所有节点按照data大小顺序依次排列, 规定链表头部 存储的data值是最大的, 而链表尾部
    存储的data值是最小的.
    """
    # ---------------嵌套类: 用于辅助外面的类--------------------------------
    class Node:
        """
        Goal:
            使用节点作为每个元素的存储单元.
        说明:
            1. 每个存储单元有两个信息
                1.1 存储的数据 -- Field: data
                1.2 节点的指向信息-- Field: next
            2. 节点初始化时的状态
                2.1 存储的数据为 给定的数据 -- data = item
                2.2 节点指向None   -- next = None
        """
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    # --------------------嵌套类: end----------------------------------------

    def __init__(self):
        """
        Goal:
            创建 Node-based 的序列, 完成 Array-based 同样的功能.
        说明:
            1.维持head 和 tail 两个标记信息,用于支持 从头部和尾部快速添加和删除操作
            O(1) 时间内.

            2.维持 size 信息, 在O(1)时间内完成 长度查询工作.

        说明2:
            初始化时:
            1. 因为链表中没有节点, 所以 head 和 tail 皆为 None, size=0
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """
        说明: 重载len()方法, 用于支持长度查询. 因为链表维持了size信息,所以可以在O(1)
            时间内完成查询
        """
        return self.size

    def add(self, item):
        """
        Goal:
            将节点插入根据大小顺序合适的位置.
        Description:
            1. 当链表为空时, 添加 new_node. 此时这是链表中唯一的一个节点,
            它既是头部,亦是尾部.

            2. 当链表中有至一个节点时,添加 new_node.
            链表特征:
                链表按照节点中的data大小顺序,将节点从大到小依次排列. 链表的头部
                是data为最大的节点,尾部是data为最小的节点.
            比较过程:
                2.1 先和链表的头部进行比较,如果 new_node.data > self.head.data,
                    那么new_node就应该变成新的头部:
                    2.1.1 将new_node 指向 头部节点
                    2.2.2 链表头部 指向 new_node
                2.2 依次进行比较. 发现 new_node.data > x.data, 那么:
                    2.2.1 x的上一个节点指向 new_node
                    2.2.2 new_node 指向 x节点
                2.3 比较到最后, new_node.data比链表中任何一个节点的 data都小,那么
                    这个节点应该成为链表新的尾部:
                    2.3.1 链表原来尾部指向 new_node
                    2.3.2 链表的尾部指向 new_node
                    2.3.3 (略) 链表尾部指向None,因为 new_node 诞生时自动指向None,
                    所以这一步可以忽略.

            3. size + 1
            """
        new_node = self.Node(item)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if new_node.data > self.head.data:
                new_node.next = self.head
                self.head = new_node
            elif new_node.data < self.tail.data:
                self.tail.next = new_node
                self.tail = new_node
            else:
                previous = self.head
                start = previous.next
                for _ in range(self.size - 1):
                    if new_node.data > start.data:
                        previous.next = new_node
                        new_node.next = start
                    else:
                        previous = previous.next
                        start = start.next
        self.size += 1

    def index_to_value(self, index=0):
        """
        Goal: 完成同list[i]相同的功能,根据索引查找对应的值
        """
        start = self.head
        # print(start.data)
        for _ in range(index):
            start = start.next
        return start.data

    def index(self, item):
        """
        Goal: 根据item的值返回链表中相应的索引
        """
        start = self.head

        for i in range(self.size):
            if start.data == item:
                return i
            start = start.next
        return "Index failed: there is no such item"

    def search(self, item):
        result = self.index(item)
        if type(result) == int:
            return True
        else:
            return result

    def remove(self, item):
        """
        Goal: 移除链表中的某一个值

        Description:
            1. 当链表为空时, 不能移除
            2. 当链表只有一个值时, 移除这个这个值, 链表为空, 头尾标记都指向 None
            3. 当链表长度多于一个值: 移除 有以下三种情况:
                3.1 移除的值是头部节点
                    3.1.1 原来的头部节点指向None
                    3.2.2 头部指向 原来头部节点的下一节点
                3.2 移除的值是尾部节点
                    3.2.1 原来尾部节点的上一节点指向None
                    3.2.2 尾部指向 原来尾部节点的上一节点
                3.3 中间节点

        """
        if self.size == 0:
            return "Remove failed: Linked List is empty"
        if self.size == 1 and self.head.data == item:
            self.tail = None
            self.head = None
            self.size -= 1
        if self.size >= 2:
            start = self.head
            for i in range(self.size):
                if start.data != item:
                    previous = start
                    start = start.next
                else:
                    if i == 0:
                        temp = self.head.next
                        start.next = None
                        self.head = temp
                        self.size -= 1
                        return None
                    elif i == self.size - 1:
                        previous.next = None
                        self.tail = previous
                        self.size -= 1
                        return None
                    else:
                        previous.next = start.next
                        start.next = None
                        self.size -= 1
                        return None
        return "Remove failed: No such item"


if __name__ == '__main__':
    L = OrderedList()
    L.add(10)           # None <- 10

    L.add(30)           # None <- 10 <- 30

    L.add(20)           # None <- 10 <- 20 <- 30
    L.add(5)            # None <- 5  <- 10 <- 20 <- 30
    print(L.index_to_value(3))  # return 5
    print(L.index(5))         # return 3
    print(L.index(9))   # Index failed
    print(L.search(5))  # return True
    print(L.search(9))  # Index failed
    print(L.remove(8))  # Remove failed: no such item
    print(L.remove(30))  # return None     None <- 5 -< 10 <- 20
    print(L.index_to_value(0))   # return 20
    print(L.remove(10))  # Return  None <- 5 <- 20
    print(len(L))   # return 2




