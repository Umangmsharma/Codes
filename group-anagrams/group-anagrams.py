class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
       dic=defaultdict(list)
       print(" dic ", dic)


       for i in strs:
           print(i,"\n")
           dic["".join(sorted(i))].append(i)
       print(dic.values())


       return dic.values()