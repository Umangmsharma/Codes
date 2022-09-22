class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        i = len(digits) - 1
        
        if digits[i] < 9:
            digits[i] +=1
            return digits
        elif digits[i] == 9 and i == 0:
            return [1,0]
        
        carry = 1
        while carry > 0 and i >= 0 :
            plus_one = digits[i] + 1
            carry = plus_one // 10
            digits[i] = plus_one % 10
            i -= 1
            
        if carry :
            digits.insert(0, carry)
            
        return digits