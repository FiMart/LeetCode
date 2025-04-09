from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_time = 0
        
        for i in range(1, len(timeSeries)):
           time_diff = timeSeries[i] - timeSeries[i - 1]
           total_time += min(time_diff, duration)

        total_time += duration
        return total_time