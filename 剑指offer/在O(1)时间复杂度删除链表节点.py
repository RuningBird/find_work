class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def deleteNode(self, node):
    if node is None:
        return
    elif node.val == node.next is None:
        node = None
    # elif