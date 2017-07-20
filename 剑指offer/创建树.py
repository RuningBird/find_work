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


def create_tree(root, queue):
    root = None
    val = queue.pop()
    if val is not '#':
        root = TreeNode(int(val))
        root.left = create_tree(root.left, queue)
        root.right =create_tree(root.right, queue)
    return root

def make_tree(root, str_seq):
    queue = list(str_seq)
    queue.reverse()
    root = create_tree(root,queue)
    return root

# str_pre = '12##3##'
# queue = list(str_pre)
# queue.reverse()
#
#
# root = None
# root2 = create_tree(root, queue)
# print_tree(root2)
