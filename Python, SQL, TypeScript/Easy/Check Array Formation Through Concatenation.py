class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i < len(arr):
            found = False
            for piece in pieces:
                if arr[i:i + len(piece)] == piece:
                    i += len(piece)
                    found = True
                    break
            if not found:
                return False
        return True