class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in wall:
            total = 0
            for i in range(len(row) - 1):
                total += row[i]
                count[total] += 1
        max_count = max(count.values(), default=0)
        return len(wall) - max_count if max_count else len(wall)