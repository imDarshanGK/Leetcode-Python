class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_world = words[-1]
        length = len(last_world)
        return length
