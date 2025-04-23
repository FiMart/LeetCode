"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traversal(root):
            if not root: return
            for child in root.children:
                traversal(child)
            ret.append(root.val)
        ret = []
        traversal(root) 
        return ret