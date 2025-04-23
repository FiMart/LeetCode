# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Check if the current node is a duplicate
            if current.next and current.val == current.next.val:
                # Skip all duplicates
                while current.next and current.val == current.next.val:
                    current = current.next
                # Link to the next distinct value
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next