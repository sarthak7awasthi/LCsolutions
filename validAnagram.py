class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            Dict={}
            Dict2={}
            for i in s:
                if Dict.get(i):
                    Dict[i]+=1
                else:
                    Dict[i]=1
            for i in t:
                if Dict2.get(i):
                    Dict2[i]+=1
                else:
                    Dict2[i]=1
            if Dict==Dict2:
                return True
            else:
                return False
        else:
            return False