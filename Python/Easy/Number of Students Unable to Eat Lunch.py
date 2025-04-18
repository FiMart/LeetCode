class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for sandwich in sandwiches:
            if cnt[sandwich] == 0:
                break
            cnt[sandwich] -= 1
        return sum(cnt.values())