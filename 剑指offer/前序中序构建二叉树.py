class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def print_tree(tree):
    if tree is None:
        return
    print(tree.val, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)


def buildTree(preorder, inorder):
    if len(preorder) is 0 or len(inorder) is 0:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)  # 创建节点

    pos = inorder.index(root_value)  # 找到inorder中间位置
    inorder_left = inorder[:pos]  # 中序左子树
    inorder_right = inorder[pos + 1:]  # 中序右子树

    preorder_left = preorder[1:pos + 1]  # 先序左子树
    preorder_right = preorder[pos + 1:]  # 先序右子树

    root.left = buildTree(preorder_left, inorder_left)  # 递归创建左子树
    root.right = buildTree(preorder_right, inorder_right)  # 递归创建右子树

    return root


pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
in_order = [4, 7, 2, 1, 5, 3, 8, 6]

tree = buildTree(pre_order, in_order)

print_tree(tree)

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
# node2.left = None

root.left = node1
root.right = node2
print_tree(root)

