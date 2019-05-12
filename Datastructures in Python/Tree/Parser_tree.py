'''
本部分代码是 建立分析树： build tree

之后要 遍历树 来计算值:

'''
from class_tree import BinaryTree
import operator


class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':    # 遇见新的表达式， 新建并追踪一颗左子树
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:  # 遇见操作数，写入值，追踪其父树
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:  # 遇见运算符，写入符号，新建并追踪右子树
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':  # 遇见表达式结尾， 追踪其父树
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):

    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/':  operator.truediv,
             }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


# if __name__ == '__main__':
    # pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    # print('1')
    # print(evaluate(pt))
