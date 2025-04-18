class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev = ''
        for i in words:
            if sorted(i) != sorted(prev):
                ans.append(i)
            prev = i
        return ans