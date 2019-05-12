class BinaryTree:
    """
    每一个节点都是一颗二叉树。每棵二叉树由左子树，右子树和根组成。
    同时，我们维护一个记录数节点的字段size.
    """
    # ---------------Constructor --------------------------------------
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rigthChild = None
        self.size = 0

    # -------------add -------------------------------------------------
    def insertLeft(self, newNode):
        """
        在根节点的左侧插入一个子树，原来的左子树 成为 新子树 的左子树
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        self.size += 1

    def insertRight(self, newNode):
        if self.rigthChild is None:
            self.rigthChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rigthChild = self.rigthChild
            self.rigthChild = t
        self.size += 1

    # -------------accessor---------------------------------------------
    def getRightChild(self):
        return self.rigthChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # ------------Tree traversal---------------------------------------- --
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rigthChild:
            self.rigthChild.preorder()


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())

