class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        curr, prev = 0, 0
        while i < (len(nums)):
            if (nums[i] != nums[prev]):
                curr+=1
                nums[curr] = nums[i]
            
            prev+=1      
            i+=1
                    
        return curr+1