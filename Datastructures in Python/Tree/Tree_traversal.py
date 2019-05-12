from class_tree import BinaryTree
import operator

def preorder(tree):
    """
    前序遍历：
    调用时：
    一个节点的遍历优先度
    自身，
    自身的左子节点，
    自身的右子节点 。

    调用结束时：
    如果这个节点是父节点的左子节点， 那么下次调用的就是父节点的右子节点
    如果这个节点是父节点的右子节点， 那么就要看父节点 是 爷节点的什么节点了。
    只要这个节点有兄弟， 那么就调用兄弟， 然后父节点有兄弟，就调用父节点的兄弟，
    然后依次向上查看
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def postordereval(tree):
    opers = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '': operator.truediv,
            }

    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:   # 如果左右子节点的值都算了出来
            return opers[tree.getRootVal()](res1, res2)  # 进行计算
        else:
            return tree.getRootVal()    # 如果是叶节点,那么就保存它的值


def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal)
        inorder(tree.getRootChild())


def printexp(tree):
    if tree:
        Sval = '(' + printexp(tree.getLeftChild())
        Sval += str(tree.getRootVal())
        Sval += printexp(tree.getRootChild()) + ')'
        return Sval


def printexp_noP(tree):
    if tree:
        Sval = printexp(tree.getLeftChild())
        Sval += str(tree.getRootVal)
        Sval += printexp(tree.getRootChild())
