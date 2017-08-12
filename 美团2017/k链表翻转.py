class LNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def show(self):
        p = self
        while p:
            print(p.val, end=' ')
            p = p.next
        print('\n')


# 翻转整个链表
def reverse_all(head):
    hres = LNode(0)
    q = head
    while q:
        tmp =q
        q = q.next

        tmp.next = hres.next
        hres.next = tmp


    res = hres.next
    return res

'''
@:parameter head 待翻转链表
@:parameter k  翻转位置
'''
def k_reverse(head, k):
    res = None
    if head:
        pk = 0
        head2 = None  # k节点之后的链表
        p = head
        while pk < k and p:
            p = p.next
            pk += 1
        if p:  # k<=链表长度
            nhead = LNode(0)
            q = head

            while q != p:
                tmp = q
                q = q.next

                tmp.next = nhead.next
                nhead.next = tmp

            tail = nhead  # 前半部分尾指针
            while tail.next:
                tail = tail.next

            tail.next = p

            res = nhead.next
            return res

        else:  # k>链表长度，直接翻转整个链表
            res = reverse_all(head)
            return res

        pass
    else:  # 链表为空
        return res

#  测试用例
node1 = LNode(1)
node2 = LNode(2)
node3 = LNode(3)
node4 = LNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

node1.show()# 显示原链表

res = k_reverse(node1, 2)
res.show() # k翻转之后链表
