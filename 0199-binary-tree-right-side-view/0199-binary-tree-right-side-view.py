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

        hm = defaultdict(list)

        queue = deque([(root, 0)])
        ans = []

        while queue:

            node, row = queue.popleft()

            if node:

                hm[row].append(node.val)


            if node and node.left:
                queue.append((node.left, row+1))

            if node and node.right:
                queue.append((node.right, row+1))

        for key, value in hm.items():
            ans.append(value[-1])

        return ans
            
        