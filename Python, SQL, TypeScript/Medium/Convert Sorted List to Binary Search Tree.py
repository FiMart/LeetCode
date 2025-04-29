# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        # Function to find the middle element of the linked list
        def find_middle(left, right):
            slow = left
            fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Recursive function to convert the linked list to BST
        def convert_list_to_bst(left, right):
            if left == right:
                return None
            
            mid = find_middle(left, right)
            node = TreeNode(mid.val)
            
            node.left = convert_list_to_bst(left, mid)
            node.right = convert_list_to_bst(mid.next, right)
            
            return node
        
        return convert_list_to_bst(head, None)