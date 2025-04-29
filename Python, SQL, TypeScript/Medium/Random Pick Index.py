import random
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        # Create a hashmap to store indices for each number
        self.num_indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_indices[num].append(i)

    def pick(self, target: int) -> int:
        # Randomly select an index from the list of indices for the target
        indices = self.num_indices[target]
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)