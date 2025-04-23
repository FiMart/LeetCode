class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        for word in s.split():
            if word.isdigit():
                curr = int(word)
                if curr <= prev:
                    return False
                prev = curr
        return True