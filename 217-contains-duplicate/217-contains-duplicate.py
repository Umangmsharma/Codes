class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_uniq = set()
        
        for i in nums:
            if i in num_uniq:
                return True
            
            num_uniq.add(i)
        return False