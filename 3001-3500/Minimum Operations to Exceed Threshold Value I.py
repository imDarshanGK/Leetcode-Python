class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
                return bisect_left(sorted(nums), k)
