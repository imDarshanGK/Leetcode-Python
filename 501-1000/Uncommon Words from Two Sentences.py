class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split() + s2.split())
        uncomman = []
        for word in count:
            if count[word] == 1:
                uncomman.append(word)
        return uncomman