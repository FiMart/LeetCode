class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_length = 0

        for i in range(len(nums)):
            if not visited[i]:
                current_length = 0
                current_index = i

                while not visited[current_index]:
                    visited[current_index] = True
                    current_index = nums[current_index]
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length