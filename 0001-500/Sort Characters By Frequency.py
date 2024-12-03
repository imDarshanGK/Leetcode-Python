class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_chars = sorted(frequency.items(), key = lambda x: -x[-1])
        result = ''.join([char * count for char, count in sorted_chars])
        return result