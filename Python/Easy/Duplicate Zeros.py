class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1
        j = n + zeros - 1

        while i >= 0:
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
                if j < n:
                    arr[j] = 0
                j -= 1
            else:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
            i -= 1