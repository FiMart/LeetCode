"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to hold the mapping from original node to cloned node
        clone_map = {}

        # Helper function for DFS
        def dfs(original_node):
            if original_node in clone_map:
                return clone_map[original_node]

            # Create a new node for the cloned graph
            clone_node = Node(original_node.val)
            clone_map[original_node] = clone_node

            # Recursively clone the neighbors
            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        return dfs(node)