class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1[0], event1[1]
        start2, end2 = event2[0], event2[1]

        return not (end1 < start2 or end2 < start1)