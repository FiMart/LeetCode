class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        setA = set(aliceSizes)
        delta = (sumA - sumB) // 2
        for b in bobSizes:
            if b + delta in setA:
                return [b + delta, b]
        return []