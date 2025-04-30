# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            count[total_sum] += 1
            return total_sum

        from collections import defaultdict
        count = defaultdict(int)
        dfs(root)
        max_count = max(count.values())
        return [s for s, c in count.items() if c == max_count]