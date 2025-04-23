class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2
                if abs(num - arr2[mid]) <= d:
                    break
                elif arr2[mid] < num - d:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                count += 1
        return count