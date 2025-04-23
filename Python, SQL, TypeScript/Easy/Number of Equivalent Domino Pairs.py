class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        for a, b in dominoes:
            count[(min(a, b), max(a, b))] += 1
        return sum(v * (v - 1) // 2 for v in count.values())