"""
ADT 接口:
BinaryHeap()  创建一个新的,空的,二叉堆
insert(k)  在堆中添加一个新的项
finMin()   寻找并返回堆中有最小值的项, 但是不移除
delMin()   移除兵返回堆中最小值的项
isEmpty() 测试堆是否为空
size ()     返回堆节点的项的数量
buildHeap() 从一个列表中建立一个新的堆
"""


class BinHeap:
    def __init__(self):
        """
        构造器目标:
        1. 使用合适的基础数据结构来表示想要构造的数据结构
        2. 记录数据的数量
        """
        self.heapList = [0]
        self.currentSize = 0

    def __len__(self):
        return self.currentSize

    def perUP(self, i):
        """
        增加函数的工具
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def insert(self, k):
        """
        初始化数据结构之后所进行的操作就是: 增,删,查,改
        """
        self.heapList.append[k]
        self.currentSize += 1
        self.perUP(self.currentSize)

    def perdown(self, i):
        while i <= self.currentSize // 2:
            mc = self.min_child(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        """
        1. 交换第一个元素和最后一个元素
        2. 弹出最后一个元素
        3. 维护最小堆的性质
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.perdown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perdown(i)
            i -= 1


if __name__ == '__main__':
    alist = [9, 6, 5, 2, 3]
    aheap = BinHeap()
    aheap.buildHeap(alist)
    for i in range(len(aheap)):
        print(aheap.heapList[i])






