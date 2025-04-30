# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            return (curr_sum == targetSum) + dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

        if not root:
            return 0

        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)