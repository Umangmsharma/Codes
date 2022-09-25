class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = []
        
        for i in range (1,numRows+1) :
            
            if i == 1 :
                pascal.append([1])
                continue
                
            temp_lis = []
            for j in range (i):
                if j >0 and j < i-1:
                    num = pascal[i-2][j-1] + pascal[i-2][j]
                    temp_lis.append(num)
                else :
                    num = 1
                    temp_lis.append(num)


                    
            pascal.append(temp_lis)
            
        return pascal