class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common_elements = set1.intersection(set2)
        if common_elements:
            return min(common_elements)
        return min(nums1) * 10 + min(nums2) if min(nums1) < min(nums2) else min(nums2) * 10 + min(nums1)