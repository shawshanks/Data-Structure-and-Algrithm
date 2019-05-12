def deleteMin(self):
    self.root = self._deleteMin(self.root)


def _deleteMin(self, node):
    if node.left is None:
        return node.right
    node.left = self._deleteMin(node.left)
    node.size = self._size(node.left) + self._size(node.right) + 1
    return node



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
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        t = node    # node to delete
        x = min(t.right)    # successor= the node with the smallest key in its
                            # right subtree (the most left node in the subtree)
        # 后继者作为被删除节点的替换
        x.right = self._deleteMin(t.right)
        x.left = t.left


