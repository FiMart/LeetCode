class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        for i in arr:
            if cnt[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""