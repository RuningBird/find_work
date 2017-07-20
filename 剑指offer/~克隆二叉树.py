import 剑指offer.创建树 as mk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


res = []


def ct(root, tree):
    if root:
        tree = TreeNode(root.val)
        res.append(tree.val)
        tree.left = ct(root.left, tree.left)
        tree.right = ct(root.right, tree.right)
    else:
        return None


t = None


def ct1(root, t):
    if root:
        t = TreeNode(root.val)
        res.append(t.val)

        t.left = ct(root.left, t.left)
        t.right = ct(root.right, t.right)
    else:
        return None


tr_seq = "122##3##4##"
root = None
t1 = mk.make_tree(root, tr_seq)
mk.print_tree(t1)

tr2 = None
# ct(t1, tr2)
ct1(t1, tr2)
print(tr2)
