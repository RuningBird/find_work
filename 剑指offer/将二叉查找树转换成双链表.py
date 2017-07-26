# not pass
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
        if root:
            self.io(root)
            return self.make_dList()
        else:
            return None

    def make_dList(self):
        self.res.reverse()
        if self.res:
            self.head = DoublyListNode(0)
            tail = self.head

        while self.res:
            val = self.res.pop()
            s = DoublyListNode(val)

            s.next = tail.next
            s.prev = tail
            tail.next = s  # 尾插法

            tail = tail.next

        self.head = self.head.next
        return self.head

    def show_dList(self):
        p = self.head
        while p:
            print(p.val, end=' ')
            p = p.next

    def io(self, root):  # 中序遍历二叉树
        if root:
            self.io(root.left)
            self.res.append(root.val)
            self.io(root.right)


ls = [1, 2, 3, 4, 5]
so = Solution()
so.res = ls
so.make_dList()
so.show_dList()
