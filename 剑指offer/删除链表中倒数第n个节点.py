class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def show_list(lis):
    if not lis:
        print(lis)
        return
    if isinstance(lis, ListNode):
        p = lis
        while p:
            print(p.val, end=' ')
            p = p.next


def removeNthFromEnd(head, n):
    if not head:
        return None
    elif not head.next:
        return None

    p1 = head
    p2 = None

    for i in range(n - 1):
        p1 = p1.next

    p2 = head
    while p1.next:
        p1 = p1.next
        p2 = p2.next

    p2.val = p2.next.val
    p2.next = p2.next.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# removeNthFromEnd(n1,2)
tmp = removeNthFromEnd(n5,1)
show_list(tmp)
