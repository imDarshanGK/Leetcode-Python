class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        total = count * (count+1)//2
        return total - sum(nums)
