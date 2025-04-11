class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        
        count_target = Counter(target)
        count_arr = Counter(arr)
        
        return count_target == count_arr