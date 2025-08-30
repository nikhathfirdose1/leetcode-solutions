# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([(root, 0)])
        min_idx, max_idx = 0,0

        column = defaultdict(list)

        ans = []

        while queue:

            node, col = queue.popleft()

            if node is not None:
                column[col].append(node.val)
                min_idx = min(min_idx, col)
                max_idx = max(max_idx, col)

                if node.left:
                    queue.append((node.left, col-1))

                if node.right:
                    queue.append((node.right, col +1))

        
        for col in range(min_idx, max_idx+1):
            ans.append(column[col])

        return ans



        