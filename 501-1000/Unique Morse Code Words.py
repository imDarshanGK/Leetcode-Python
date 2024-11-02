class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
      morse_mapping = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", 
            ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
      unique_transformations = set()
      for word in words:
        morse_code = ''.join(morse_mapping[ord(char) - ord('a')] for char in word)
        unique_transformations.add(morse_code)
      return len(unique_transformations)

