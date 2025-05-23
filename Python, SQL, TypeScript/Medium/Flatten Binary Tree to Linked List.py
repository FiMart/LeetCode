# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store the right subtree
        right_subtree = root.right
        
        # Move the left subtree to the right
        root.right = root.left
        root.left = None
        
        # Find the end of the new right subtree and attach the original right subtree
        current = root
        while current.right:
            current = current.right
        current.right = right_subtree