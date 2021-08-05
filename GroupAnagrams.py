class Solution:
    def check(self,s1,s2):
        if sorted(s1)==sorted(s2):
            return True
        return False        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict={}
        Dict[tuple(sorted(strs[0]))]=[strs[0]]
        for k in range(1,len(strs)):
            found=False
            if Dict.get(tuple(sorted(strs[k]))):
                
                Dict[tuple(sorted(strs[k]))].append(strs[k])
                   
            else:
                Dict[tuple(sorted(strs[k]))]=[strs[k]]
        strs=list(Dict.values())
        return strs
