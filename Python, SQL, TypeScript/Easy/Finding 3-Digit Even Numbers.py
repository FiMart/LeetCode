class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        digits.sort()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if i == k or j == k:
                        continue
                    if digits[k] % 2 == 0:
                        ans.append(digits[i] * 100 + digits[j] * 10 + digits[k])
        return sorted(list(set(ans))) if len(ans) > 0 else []