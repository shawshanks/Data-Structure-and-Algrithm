"""
Circulary Linked.py 中的CircularLinkedList 类 的环状链表结构 有着以下不便:

----------------------------原始模型缺点----------------------------------
1. add() 操作
1.1  要分成三种情况:
        链表为空 ,add()操作使得链表形成一个点
        链表只有一个节点, add()操作使得链表形成一个环
        链表多于两个节点, add()操作, 对环状结构进行操作
    这三种情况不仅涉及到 节点本身的操作, 还要涉及到 cur标记的操作,不同情况下的操作
    都有微小的差异.

2 remove()操作
2.1 也要分成三种情况:
       无节点, 一个节点, 两个节点以上(环状)



--------------------------原始模型缺点分析------------------------------------
这两种操作是最为麻烦的. 模型的不统一是导致 必须区分不同情况的根本原因. 所以要想办法
减少必须区分的情况. 最好是统一模型, 只有一种情况.




--------------------------解决方法: 添加哨兵统一为环状结构 --------------------
可以 添加两个 哨兵节点(Sentinels), 这两个 sentinels nodes 互相 指向对方,形成一个
环状结构.

e.g:             S1 <--> S2
i.e.:           S1.next = S2
                S2.next = S1

为了方便,使用 head表示S1, 使用tail表示S2
那么无论是 add()还是remove()操作,都只涉及环状结构操作, 这会大大减少我们的工作量.

-----------------------扩展使用 ------------------------------------------------
当然, 也可以在单向非环形链表中使用 哨兵. 也能大大减少工作量
"""


class Sitienel_Circularly:
    # ---------------Nested Node class ------------------------------------
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    # ---------------- end -------------------------------------------------
    S1 = Node(None)  # 为了方便, 这两个特殊节点的data field都为空
    S2 = Node(None)
    S1.next = S2
    S2.next = S1

    def __init__(self, head=S1, tail=S2):
        self.head = head
        self.tail = tail
        self.size = 0

    def add(self, item):
        """
        为了方便,规定插入的新节点永远在 head后.
        add(10)    head -> 10 -> tail -> (head)  其中-> (head)表示形成环状
        add(20)    head -> 20 -> 10 -> tail -> (head)
        add(30)    head -> 30 -> 20 -> 10 -> tail -> (head)
        add(15)    head -> 15 -> 30 -> 20 -> 10 -> tail -> (head)
        """
        new_node = self.Node(item)
        new_node.next = self.head.next
        self.head.next = new_node

        self.size += 1

    def remove(self, item):
        previous = self.head     # 从head的下个节点开始寻找,同时维持 上个节点的信息
        start = self.head.next

        for i in range(self.size):
            if not start.data == item:
                previous = start
                start = start.next
            else:
                previous.next = start.next
                start.next = start.data = None  # 销毁节点
                self.size -= 1
                return "Success!"
        return "Remove failed: Didn't find such item"

    def __len__(self):
        return self.size


if __name__ == '__main__':
    L = Sitienel_Circularly()
    L.add(10)      # head -> 10 -> tail
    L.add(20)      # head -> 20 -> 10 -> tail
    L.add(15)      # head -> 15 -> 20 -> 10 ->tail
    print(len(L))   # return 3
    print(L.head.next.data)  # return 15
    print(L.remove(10))
    print(L.remove(20))











