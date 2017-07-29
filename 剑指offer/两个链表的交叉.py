class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        # return self.gsn(headA,headB)
        return self.stack_method(headA, headB)

    # 推荐方法*****
    # 统计链表长度，从等长处开始查找
    def gsn(self, ha, hb):
        len_ha = 0
        len_hb = 0
        if ha and hb:
            p = ha
            while p:
                len_ha += 1
                p = p.next
            p = hb
            while p:
                len_hb += 1
                p = p.next
            len_sub = 0
            p = ha
            q = hb
            if len_ha > len_hb:
                len_sub = len_ha - len_hb
                for i in range(len_sub):
                    p = p.next
            else:
                len_sub = len_hb - len_ha
                for i in range(len_sub):
                    q = q.next
            while p:
                if p.val == q.val:
                    return p
                p = p.next
                q = q.next
            return p

    # 栈方法，从后往前找交叉节点
    def stack_method(self, ha, hb):
        if ha and hb:
            p, q = ha, hb
            sa = sb = []
            while p:
                sa.append(p)
                p = p.next

            while q:
                sb.append(q)
                q = q.next

            res = None
            while sa and sb:
                p, q = sa.pop(), sb.pop()
                if p.val == q.val:
                    res = p
            return res

    # 蛮力法
    def qiongju(self, ha, hb):
        if ha and hb:
            p = ha
            while p:
                q = hb
                while q:
                    if p.val == q.val:
                        return p
                    q = q.next
                p = p.next

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(2)
b3 = ListNode(3)