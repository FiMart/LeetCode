class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = {}
        
        for num in nums:
            if num - k in num_count:
                count += num_count[num - k]
            if num + k in num_count:
                count += num_count[num + k]
            num_count[num] = num_count.get(num, 0) + 1
        
        return count