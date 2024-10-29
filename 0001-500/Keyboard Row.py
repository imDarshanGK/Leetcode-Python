class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        for word in words:
            if set(word.lower()) <= set("qwertyuiop"):
                output.append(word)
            elif set(word.lower()) <= set("asdfghjkl"):
                output.append(word)
            elif set(word.lower()) <= set("zxcvbnm"):
                output.append(word)
        return output

        