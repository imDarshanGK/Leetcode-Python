class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index = []
        for indexvalue, word in enumerate(words):
            if x in word:
                index.append(indexvalue)
        return index