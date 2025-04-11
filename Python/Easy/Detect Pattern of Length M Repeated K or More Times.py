class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            if arr[i:i + m] == arr[i + m:i + m * 2]:
                count = 2
                while count < k and arr[i:i + m] == arr[i + count * m:i + (count + 1) * m]:
                    count += 1
                if count == k:
                    return True
        return False