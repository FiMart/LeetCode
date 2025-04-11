class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current = 1
        index = 0
        
        while missing_count < k:
            if index < len(arr) and arr[index] == current:
                index += 1
            else:
                missing_count += 1
            
            if missing_count < k:
                current += 1
        
        return current