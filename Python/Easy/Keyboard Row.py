class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Initialize an empty list to store the valid words.
        valid_words = []
      
        # Mapping for each letter to its corresponding row on the keyboard.
        row_mapping = "12210111011122000010020202"
      
        # Iterate over each word in the provided list.
        for word in words:
            # Get the row for the first character of the word (convert to lowercase for uniformity).
            first_char_row = row_mapping[ord(word[0].lower()) - ord('a')]
          
            # Check if all characters in the word are in the same row as the first one.
            if all(row_mapping[ord(char.lower()) - ord('a')] == first_char_row for char in word):
                # If they are, append the word to our list of valid words.
                valid_words.append(word)
      
        # Return the list of valid words that can be typed using letters of one row on the keyboard.
        return valid_words