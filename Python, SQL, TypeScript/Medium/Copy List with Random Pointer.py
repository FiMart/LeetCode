"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create a mapping from original nodes to new nodes
        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Set the next and random pointers for the new nodes
        current = head
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new.get(current.next)
            new_node.random = old_to_new.get(current.random)
            current = current.next

        # Step 3: Return the head of the copied list
        return old_to_new[head]