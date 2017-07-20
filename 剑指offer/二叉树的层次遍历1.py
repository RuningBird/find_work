import 剑指offer.创建树 as mk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    res = []
    queue = []

    def levelOrder(self, root):
        if not root:
            return []
        self.queue.insert(0, root)
        while self.queue:
            lres = []
            qu = self.queue[:]
            self.queue = []
            while qu:
                node = qu.pop()
                lres.append(node.val)
                if node.left:
                    self.queue.insert(0, node.left)
                if node.right:
                    self.queue.insert(0, node.right)
            self.res.append(lres)
        return self.res

    def show_lt(self, root):
        self.levelOrder(root)
        print(self.res)


tr_seq = "122##3##45####"
tr_seq1 = '1248###5##36##7##'
root = None
tree = mk.make_tree(root, tr_seq1)
mk.print_tree(tree)

Solution().show_lt(tree)
