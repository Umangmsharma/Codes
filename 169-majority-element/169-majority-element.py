class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict = {}
        for i in nums:
            if i in Dict :
                Dict[i] +=1
            else :
                Dict[i] = 1
                
        return max(Dict, key=Dict.get)