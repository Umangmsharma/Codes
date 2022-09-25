class Solution:
    def isHappy(self, n: int) -> bool:
        digit_sum = 0
        dig_hash = []

        while n > 0 :
            digit = n % 10
            digit_sum += digit ** 2
            n = n // 10

            if digit_sum == 1 and n == 0:
                return True
            
            if n == 0 :
                if digit_sum not in dig_hash :
                    n = digit_sum
                    digit_sum = 0
                    dig_hash.append(n)
                
        return False