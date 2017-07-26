class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        h2 = RandomListNode(0)  # 新表头节点
        tail = h2  # 新表尾指针

        p = head
        while p:
            s = RandomListNode(p.label)  # 复制当前节点的值
            s.random = p.random  # 复制random值

            s.next = tail.next
            tail.next = s  # 尾插法建立新链表
            tail = tail.next

            p = p.next  # 指向下一个节点

        return h2.next
