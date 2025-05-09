# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)
            rob = node.val + left_not_rob + right_not_rob
            not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            return rob, not_rob
        
        return max(dfs(root))