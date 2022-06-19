class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        l = end = len(nums) - 1
        
        while start < end :
            if nums[start] + nums[end] == target :
                return [start,end]
            
            end -= 1
            if end <= start:
                end = l
                start += 1
            
        return []