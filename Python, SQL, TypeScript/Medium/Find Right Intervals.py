class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n
        sorted_intervals = sorted((start, i) for i, (start, end) in enumerate(intervals))
        
        for i, (start, end) in enumerate(intervals):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if sorted_intervals[mid][0] >= end:
                    ans[i] = sorted_intervals[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
        
        return ans