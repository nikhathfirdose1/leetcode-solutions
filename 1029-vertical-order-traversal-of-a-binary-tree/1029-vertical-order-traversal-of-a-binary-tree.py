# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:


        if not root:
            return []

        queue = deque([(root, 0,0)])
        hm = defaultdict(list)
        ans = []
        

        min_col, max_col = 0,0

        while queue:

            node, col, row = queue.popleft()

            if not node:
                continue

            hm[col].append((row,node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)


            if node.left:
                queue.append((node.left,col-1, row+1))

            if node.right:
                queue.append((node.right,col+1 ,row+1))

        for col in range(min_col, max_col+1):
            final = hm[col]
            final.sort(key=lambda x : (x[0], x[1]))
            cols = []
            for row, val in final:
                cols.append(val)
            ans.append(cols)

        return ans



        


        