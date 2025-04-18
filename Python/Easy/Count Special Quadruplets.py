class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        # Iterate through all combinations of i, j, k
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Calculate the sum of nums[i], nums[j], nums[k]
                    sum_ijk = nums[i] + nums[j] + nums[k]
                    
                    # Check if there exists a valid l
                    for l in range(k + 1, n):
                        if sum_ijk == nums[l]:
                            count += 1
        
        return count