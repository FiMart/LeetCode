class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def word_to_number(word: str) -> int:
            return int(''.join(str(ord(c) - ord('a')) for c in word))

        first_num = word_to_number(firstWord)
        second_num = word_to_number(secondWord)
        target_num = word_to_number(targetWord)

        return first_num + second_num == target_num