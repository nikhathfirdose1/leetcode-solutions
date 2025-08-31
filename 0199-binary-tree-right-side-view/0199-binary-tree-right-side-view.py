# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        hm = {}

        queue = deque([(root, 0)])
        ans = []

        while queue:

            node, row = queue.popleft()
            
            if not node:
                return None
        
            hm[row] = node.val

            if node.left:
                queue.append((node.left, row+1))

            if node.right:
                queue.append((node.right, row+1))

        for key, value in hm.items():
            ans.append(value)

        return ans
            
        