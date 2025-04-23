class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Initialize the count of deletions to 0
        deletions = 0
        
        # Iterate through each column index
        for col in range(len(strs[0])):
            # Check if the current column is sorted
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    # If not sorted, increment the deletion count and break out of the loop
                    deletions += 1
                    break
        
        return deletions