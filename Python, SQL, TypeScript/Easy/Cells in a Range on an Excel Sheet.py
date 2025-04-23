class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        return [chr(i) + str(j) for i in range(ord(start[0]), ord(end[0]) + 1) for j in range(int(start[1]), int(end[1]) + 1)]