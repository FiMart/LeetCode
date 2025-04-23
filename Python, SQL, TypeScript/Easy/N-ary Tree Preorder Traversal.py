"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        def traversal(root):
            if not root: return
            ret.append(root.val)
            for child in root.children:
                traversal(child)
        ret = []
        traversal(root) 
        return ret