# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the size of each part and the number of longer parts
        part_size, extra_parts = divmod(length, k)

        # Create the result list
        result = []
        current = head

        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < extra_parts else 0)

            # Move to the end of the current part
            for j in range(part_length - 1):
                if current:
                    current = current.next

            # Disconnect the current part from the next part
            if current:
                next_part_head = current.next
                current.next = None
                current = next_part_head

            result.append(part_head)

        return result