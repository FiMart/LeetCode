# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)

        vals = []
        inorder(root)

        dummy = TreeNode(0)
        current = dummy
        for val in vals:
            current.right = TreeNode(val)
            current = current.right

        return dummy.right