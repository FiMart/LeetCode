class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        # Count the frequency of each character in the string
        freq = Counter(s)

        # Sort the characters by frequency (highest to lowest) and then by character (lexicographically)
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Build the result string based on the sorted characters and their frequencies
        result = ''.join(char * count for char, count in sorted_chars)

        return result