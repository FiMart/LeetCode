class Solution:
    def minOperations(self, s: str) -> int:
        # Count the number of 0s and 1s in the string
        count_0 = s.count('0')
        count_1 = s.count('1')
        
        # Calculate the minimum number of changes needed to make the string alternating
        # The two possible alternating patterns are '010101...' and '101010...'
        # We need to find the minimum number of changes required to match either pattern
        changes_to_01 = sum(1 for i in range(len(s)) if s[i] != str(i % 2))
        changes_to_10 = sum(1 for i in range(len(s)) if s[i] != str((i + 1) % 2))
        
        return min(changes_to_01, changes_to_10)