class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for i in range(0, len(nums) ):
            unique = nums[i] ^ unique
        
        return unique