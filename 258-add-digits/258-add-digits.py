class Solution:
    def addDigits(self, num: int) -> int:
        
        remainder = 0
        while num > 0:
            remainder = remainder +  num % 10
            num = num // 10
            if num == 0:
                if remainder > 9:
                    num = remainder
                    remainder = 0
                else :
                    break
            
        return remainder
            