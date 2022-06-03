class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
                    
        for i in range(len(nums)):
            pair = target - nums[i]
            
            if pair in hashmap and hashmap[pair] != i:
                return [i,hashmap[pair]]
        