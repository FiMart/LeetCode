class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        group_count = {}
        for i in range(1, n + 1):
            s = digit_sum(i)
            if s not in group_count:
                group_count[s] = 0
            group_count[s] += 1

        max_group_size = max(group_count.values())
        return sum(1 for size in group_count.values() if size == max_group_size)