class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)//2 -1
        start = 0
        end = len(s) - 1
        
        s = s.lower()
        while start <= end:
            if (s[start].isalnum() and s[end].isalnum()) :
                if (s[start] == s[end]):
                    start +=1
                    end -=1
                else :
                    return False
                
            elif (not s[start].isalnum()) :
                start+=1
            
            elif (not s[end].isalnum()) :
                end-=1
                
        return True
        