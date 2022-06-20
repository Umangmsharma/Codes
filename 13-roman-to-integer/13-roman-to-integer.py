class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashmap = {}
        
        hashmap["I"] = 1
        hashmap["V"] = 5
        hashmap["X"] = 10
        hashmap["L"] = 50
        hashmap["C"] = 100
        hashmap["D"] = 500
        hashmap["M"] = 1000

        integer = 0
        prev = ''
        
        for  i in s:
            match i:
                
                case 'V':
                    if prev == 'I': 
                        integer = integer - 1 + hashmap[i] - 1
                        prev = i
                    else :
                        integer = integer + hashmap[i]
                        prev = i
                    continue

                case 'X':
                    if prev == 'I':
                        integer = integer - 1 + hashmap[i] - 1
                        prev = i
                    else :
                        integer = integer + hashmap[i]
                        prev = i
                    continue

                case 'L':
                    if prev == 'X': 
                        integer = integer - hashmap['X'] + hashmap[i] - hashmap['X'] 
                        prev = i
                    else :
                        integer = integer + hashmap[i]
                        prev = i
                    continue

                case 'C':
                    if prev == 'X': 
                        integer = integer - hashmap['X'] + hashmap[i] - hashmap['X'] 
                        prev = i
                    
                    else :
                        integer = integer + hashmap[i]
                        prev = i
                    continue

                case 'D':
                    if prev == 'C': 
                        integer = integer - hashmap['C'] + hashmap[i] - hashmap['C'] 
                        prev = i
                    else :
                        integer = integer + hashmap[i]
                        prev = i
                    continue

                case 'M':
                    if prev == 'C': 
                        integer = integer - hashmap['C'] + hashmap[i] - hashmap['C'] 
                        prev = i
                    else :
                        integer = integer + hashmap[i]  
                        prev = i
                    continue

                case default :
                    integer += hashmap[i]
                    prev = i

        
        return integer