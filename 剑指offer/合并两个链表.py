class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = None
        if l1 and l2:  # l1， l2 非空
            if l1.val < l2.val:
                head = l1
                head.next = self.mergeTwoLists(l1.next, l2)
            else:
                head = l2
                head.next = self.mergeTwoLists(l1, l2.next)
        else:
            if not l1:  # 1：l1空，
                return l2
            if not l2:  # 2：l2空，
                return l1
        return head
