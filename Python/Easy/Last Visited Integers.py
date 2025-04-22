class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        count_neg_ones = 0

        for num in nums:
            if num != -1:
                seen.insert(0, num)
                count_neg_ones = 0
            else:
                count_neg_ones += 1
                if count_neg_ones <= len(seen):
                    ans.append(seen[count_neg_ones - 1])
                else:
                    ans.append(-1)
        return ans
