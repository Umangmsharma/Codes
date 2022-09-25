class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        hash_num = {}
        alpha = "A"
        col_num = 0
        for i in range(1,27):
            
            key = chr(ord(alpha))
            hash_num[key] = i
            
            alpha = chr(ord(alpha) + 1)

        if len(columnTitle) == 1:
            return hash_num[columnTitle]
        else :
            for i in range(0,len(columnTitle)):
                
                col_num = (hash_num[columnTitle[i]]) + col_num * 26
            
            return col_num