# 未通过


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def print_tree(tree):
    if tree is None:
        return
    print(tree.val, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)


# 按层创建树
def create_tree(root, queue):
    if len(queue):
        return None
    else:
        root = None
        val_mid = queue.pop()
        if val_mid is not '#':
            root = TreeNode(val_mid)
            if not len(queue):
                val_left = queue.pop()
                root.left = create_tree(root.left, queue)
            root.right = create_tree(root.right, queue)
        return root


str_pre = '123##4'
queue = list(str_pre)
queue.reverse()

root = None
root2 = create_tree(root, queue)
print_tree(root2)
