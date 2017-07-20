class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_node(self):
        p = self
        while (p is not None):
            print(p.val, end=',')
            p = p.next

    def reverse(self, head):
        # write your code here
        if head == None:
            return None
        elif head.next is None:
            return head

        nL = ListNode(0)
        while (head is not None):
            s = head
            head = head.next

            s.next = nL.next
            nL.next = s

        return nL.next

node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = None

# node0.print_node()

node0 = node0.reverse(node0)
node0.print_node()
# node0.print_node()
