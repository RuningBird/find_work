import 剑指offer.创建树 as mk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next


class Solution:
    res = []
    head = None

    def bstToDoublyList(self, root):
        pass

    def make_dList(self):
        if self.res:
            self.head = DoublyListNode(0)
        while self.res:
            val = self.res.pop()
            s = DoublyListNode(val)

            s.next = self.head.next
            self.head.next = s  # 头插法
            s.prev = self.head

        self.head = self.head.next
        return self.head.next

    def show_dList(self):
        p = self.head
        while p:
            print(p.val, end=' ')
            p = p.next

    def io(self, root):
        if root:
            self.io(root.left)
            self.res.append(root.val)
            self.io(root.right)


ls = [1, 2, 3]
so = Solution()
so.res = ls
so.make_dList()
so.show_dList()
