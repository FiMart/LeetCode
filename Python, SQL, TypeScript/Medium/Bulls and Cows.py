class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = {}
        guess_count = {}
        
        # First pass to count bulls and record counts of non-bull digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1
        
        # Second pass to count cows based on the minimum of counts in both dictionaries
        for digit in guess_count:
            if digit in secret_count:
                cows += min(secret_count[digit], guess_count[digit])
        
        return f"{bulls}A{cows}B"