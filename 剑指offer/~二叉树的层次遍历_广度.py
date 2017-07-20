import 剑指offer.创建树 as mk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    res = []
    queue = []

    def levelOrder(self, root):
        lres = []
        node = root
        lres.append(node.val)
        self.res.append(lres)

        self.queue.insert(0,node)
        while(self.queue):
            lres = []




        self.res.append([root.val])
        self.lo(root)
        return self.res



    def show_lt(self, root):
        self.levelOrder(root)
        print(self.res)


tr_seq = "122##3##45####"
root = None
tree = mk.make_tree(root, tr_seq)
mk.print_tree(tree)

Solution().show_lt(tree)
