# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            if not node:
                return '#'
            serial = f'{node.val},{dfs(node.left)},{dfs(node.right)}'
            if serial in seen:
                seen[serial] += 1
            else:
                seen[serial] = 1
            if seen[serial] == 2:
                ans.append(node)
            return serial

        seen = {}
        ans = []
        dfs(root)
        return ans