## 未通过

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def isSubtree(self, T1, T2):
        result = False
        if T2 is None:
            result = True
        elif T1 is not None:
            if T1.val == T2.val:
                result = self.sub2(T1, T2)
            if not result:
                result = self.isSubtree(T1.left, T2)
            if not result:
                result = self.isSubtree(T1.right, T2)
        return result

    def sub2(self, T1, T2):
        if T2 is None:
            return True
        if T1 is None:
            return False
        if T1.val is not T2.val:
            return False
        return self.sub2(T1.left, T2.left) and self.sub2(T1.right, T2.right)


def print_tree(tree):
    if tree is None:
        return
    print(tree.val, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)


def create_tree(root, queue):
    root = None
    val = queue.pop()
    if val is not '#':
        root = TreeNode(val)
        root.left = create_tree(root.left, queue)
        root.right =create_tree(root.right, queue)
    return root


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
#
# # s = Solution()
# # b = s.isSubtree(root, root)
# # print(b)
# print_tree(root)

########### ----------------创建树代码-------##########
# str_pre = '12##3##'
#
# queue = list(str_pre)
# queue.reverse()
# root = None
# root2 = create_tree(root, queue)
# print_tree(root2)
########### ----------------创建树代码-------##########
# print(Solution().isSubtree(root2, root2))
########### ----------------lintcode test-------##########
test_tree = '989,982,#,972,#,947,#,920,#,903,#,894,#,881,#,866,#,864,#,842,#,841,#,796,#,726,#,647,#,613,719,593,#,#,#,590,#,558,#,554,#,538,#,512,#,504,#,468,505,467,#,#,#,456,#,413,#,331,#,330,407,320,#,#,#,312,#,306,#,301,#,274,#,251,#,235,#,231,#,222,#,181,#,93,#,83,#,73,#,64,#,62,#,60,#,28,#,21,#,20,#,-32,#,-52,#,-70,#,-87,#,-98,#,-102,#,-115,#,-116,#,-139,#,-183,#,-224,#,-241,#,-263,#,-284,#,-294,#,-296,#,-320,#,-330,#,-392,#,-398,#,-407,#,-431,#,-445,#,-460,#,-463,#,-492,#,-507,#,-518,#,-539,#,-552,#,-558,#,559,#,-587,#,-673,#,-736,#,-757,#,-766,#,-767,#,-823,#,-830,#,-867,#,-875,#,-891,#,-905,#,-910,#,-924,#,-960,#,-985,#,-988'
tree_seq = test_tree.split(',')
print(tree_seq)

queue = tree_seq
queue.reverse()
root = None
root2 = create_tree(root, queue)
print_tree(root2)

print(Solution().isSubtree(root2, root2))
