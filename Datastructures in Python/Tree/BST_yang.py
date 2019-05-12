
class BST:
    # ------------------树由Node对象组成---------------------------------
    class Node:
        def __init__(self, key, value, left=None, right=None, size=0):
            # 每个Node对象都含有
            # 一对键值
            self.key = key
            self.value = value
            # 两条链接
            self.left = left
            self.right = right
            # 一个节点计数器
            self.size = size

    # -----------root变量指向BST的根节点Node对象-------------------------
    def __init__(self, root=None):
        self.root = root

    # -----------节点计数器------------------------------------
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size

    # -----------查找实现-------------------------------------
    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None
        else:
            if key < node.key:
                return self._get(node.left, key)
            elif key > node.key:
                return self._get(node.right, key)
            else:
                return node.value

    # ---------排序实现-------------------------------------------
    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, node, key, val):
        # 如果树是空的,就返回一个含有该键值对的新节点
        if node is None:
            return self.Node(key, val, 1)
        else:
            # 如果被查找的键小于根节点的键,继续在左子树中插入该键
            if key < node.key:
                node.left = self._put(node.left, key, val)
            # 如果被查找的键小于根节点的键,继续在右子树中插入该键
            elif key > node.key:
                node.right = self._put(node.right, key, val)
            else:
                # 否则,改变键原来的值
                node.val = val
            # 节点计数器
            node.size = self._size(node.left) + self._size(node.right) + 1

    # --------------查找最小键-----------------------------------
    def min(self):
        return self._min(self.root).key

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    # -----------查找最大键--------------------------------------
    def max(self):
        return self._max(self.root).key

    def _max(self, node):
        if node.right is None:
            return node
        else:
            return self._max(node.right)

    # ---------floor()方法 向下取整--------------------------------
    def floor(self, key):
        node = self._floor(self.root, key)
        if node is None:
            return None
        return node.key

    def _floor(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if node.key < key:
            return self._floor(node.left, key)
        node_t = self._floor(node.right, key)
        if node_t is not None:
            return node_t
        else:
            return node

    # ---------deleteMin() 删除最小键-----------------------------
    def deleteMin(self):
        # root 指向 _deleteMin(self.root)的节点
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, node):
        '''
        处理方式
        we go left until finding a Node that has a null left link and
        then replace the link to that node by its right link. (simply by
        returning the right link in the recursive method.)
        '''

        # 代码特点
        # 1. take a link to  Node as argument and returns a link to a Node,
        # so taht we can reflect changes to the tree by assigning the result
        # to the link used as argument.
        # 2. 如果参数节点不是被删除的节点,最终都会返回自身

        if node.left is None:   # node is the deleted node
            return node.right
        node.left = self._deleteMin(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node  # 最终返回的是被删除节点的父节点

    # -------- delete 删除指定键----------------------------------
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node  # t为要删除的节点
            node = self._min(t.right)   # node为替代的后继节点
            node.right = self._deleteMin(t.right)   # 设置替代节点的左右链接
            node.left = t.left
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    # ---------------范围查询---------------------------------------------
    def __iter__(self):
        if self.root:
            if self.left:
                for key in self.left:
                    yield key
            yield self.key
            if self.right:
                for key in self.right:
                    yield key


























