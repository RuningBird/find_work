import 剑指offer.创建树 as mk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    plist = []
    tr = None

    def cloneTree(self, root):
        self.pre_order(root)
        self.tr = self.make_tree(self.tr, self.plist)
        return self.tr

    def create_tree(self, root, queue):
        root = None
        val = queue.pop()
        if val is not '#':
            root = TreeNode(int(val))
            root.left = self.create_tree(root.left, queue)
            root.right = self.create_tree(root.right, queue)
        return root

    def make_tree(self, root, str_seq):
        queue = list(str_seq)
        queue.reverse()
        root = self.create_tree(root, queue)
        return root

    def pre_order(self, root):
        if root:
            self.plist.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
        else:
            self.plist.append('#')


tr_seq = "122##3##4##"
root = None
t1 = mk.make_tree(root, tr_seq)
s = Solution()
# s.pre_order(t1)
print(s.plist)

r2 = None
t2 = s.cloneTree(t1)
mk.print_tree(t2)
print('\n',id(t1),id(t2))
