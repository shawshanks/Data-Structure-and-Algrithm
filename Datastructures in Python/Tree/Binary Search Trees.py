"""
Map ADT 的三种完成方式:
列表
哈希表
二叉搜索树

Goal:学习 binary search trees作为键值映射的另一种方式.

Map数据结构接口:
Map() 创建新的 map
put(key, value) 实现 增改功能
get(key) 实现 查 功能
del(key) 实现 删功能
len()   记录数量
in 成员测试
"""

"""
中序遍历 与 删除有两个子节点的节点

BST的性质:
在BST中的任一节点 p(k, v):
P 的所有左子树中key 都小于 k
P 的所有右子树中key 都大于 k

中序遍历: 使用中序遍历一颗二叉树时, 键值从小到大排列

那么在删除有两个子节点的节点时, 需要找到一个合适的键值节点替补被删除节点原来的位置,
并且保证BST的性质不变.
如果用中序遍历, 可以选这个节点左右两边的值进行替补. 例如:
21, 34, 55, 58, 70, 75, 80
如果删除58 , 可以用55 或者70 替换
这两个值分别是                       图形表示
in-order predecessor 中序前任       左子树中最右侧的那个节点
in-order successor 中序后继         右子树中最左侧的那个节点
"""


class TreeNode:
    """
    每个对象都含有一对键值,两个链接,和一个节点计数器
    """
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChilde

    def hasRightChild(self):
        return self.rightChilde

    def isLefttChild(self):
        return self.parent and self.parent.leftChilde == self

    def isRightChild(self):
        return self.parent and self.parent.rightChilde == self

    def isRoot(self):
        return not self.parent

    def isleaf(self):
        return not (self.hasLeftChild() or self.hasRightChild())

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # --------------增改-----------------------------------------------

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val,
                                                parent=currentNode)
        elif key == currentNode.key:
            currentNode.payload = val
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val,
                                                 parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    # --------------查-------------------------------------------------

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            return res if res else None
        else:
            return None

    def _get(self, key, currentNode):
        if currentNode is None:
            return None
        elif key < currentNode.key:
            self._get(key, currentNode.leftChild)
        elif key == currentNode.key:
            return currentNode
        else:
            self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contain__(self, key):
        return True if self.get(key) else False

    # -------------删---------------------------------------------------

    def delete(self, key):
        if self.size == 0:
            raise KeyError("Delete failed: the tree is empty")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Delete failed: no such key")

    def remove(self, currentNode):
        if currentNode.isLeaf():    # 无子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        # 有两个子节点
        # 1. 在树中寻找能替换这个节点的子节点, 以维持搜索二叉树的性质
        # 要寻找的节点 是左子树的最右侧位置
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:   # 只有一个子节点
            if currentNode.hasLeftChild():
                currentNode.leftChild.parent = currentNode.parent
                if currentNode.isLefttChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:   # 有子无父,说明此节点是根
                    # self.root = currentNode.leftChild
                    # 或者 它和子节点的值换掉,然后把它的子节点指向原来子节点的子节点
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                            currentNode.leftChild.key,
                                            currentNode.leftChild.leftChild,
                                            currentNode.leftChild.rightChild)
            elif currentNode.hasRightChild():
                if currentNode.isLefttChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # 有子无父,说明此节点是根节点
                    # self.root = currentNode.rightChild
                    # 或者 它和子节点的值换掉,然后把它的子节点指向原来子节点的子节点
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                            currentNode.rightChild.payload,
                                            currentNode.rightChild.leftChild,
                                            currentNode.rightChild.rightChild)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elfi


