# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        def inorder(node):
            if not node:
                return []

            return inorder(node.left) + [node] + inorder(node.right)

        order = inorder(root)

        for i, node in enumerate(order):

            if node.val == p.val:
                if i == len(order) -1:
                    return None
                else:
                    return order[i+1]
                
        