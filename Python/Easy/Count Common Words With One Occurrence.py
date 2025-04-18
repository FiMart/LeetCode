class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        ans = 0
        for i in cnt1:
            if cnt1[i] == 1 and cnt2[i] == 1:
                ans += 1
        return ans