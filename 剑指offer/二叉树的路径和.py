import 剑指offer.创建树 as mk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


res = []  # 用来返回值
stack = []  # 保存路径


def binaryTreePathSum(root, target):
    bt(root, target)
    return res

 
def bt(root, target):
    if root:  # 非空树
        stack.append(int(root.val))
        if not root.left and not root.right:  # 是叶子节点
            my_sum = sum(stack)
            if my_sum == target:
                res.append(stack[:])
        bt(root.left, target)
        if root.left:
            stack.pop()
        bt(root.right, target)
        if root.right:
            stack.pop()


tr_seq = "122##3##4##"
root = None
tree = mk.make_tree(root, tr_seq)
mk.print_tree(tree)

lis = binaryTreePathSum(tree,5)
# bt(tree,5)
print(res)
print(lis)