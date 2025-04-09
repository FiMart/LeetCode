from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map each number in nums2 to its next greater element
        next_greater_map = {}
        stack = []
        
        # Process nums2 to find next greater element for each number
        for num in nums2:
            # While stack has elements and current number is greater than the top element
            while stack and num > stack[-1]:
                # Current number is the next greater element for the top element
                next_greater_map[stack.pop()] = num
            stack.append(num)
        
        # For remaining elements in stack, there's no next greater element
        for num in stack:
            next_greater_map[num] = -1
        
        # Build the result using the map
        return [next_greater_map[num] for num in nums1]