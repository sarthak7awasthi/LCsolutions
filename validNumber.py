# Passed 1318 test cases out of 1482

class Solution:
    def isNumber(self, s: str) -> bool:
        Dict={"0":"1","1":"1","2":"1","3":"1","4":"1","5":"1","6":"1","7":"1","8":"1","9":"1","e":"1","E":"1",".":"1","+":1,"-":1}
        if len(s)==1:
            if s=="e" or s=="." or s=="+" or s=="-":
                return False
            
           
            if Dict.get(s[0]):
                return True
            else:
                return False
        if s[0]=="e" or s[0]=="E":
            return False
        if s[1]=="+" or s[1]=="-":
            return False
      
            
        count=0
        for i in range(len(s)):
            
            if Dict.get(s[i]):
                if s[i]=="." or s[i]=="E" or s[i]=="e" or s[i]=="-" or s[i]=="+":
                    
                    if s[i]!="." and (i==len(s)-1):
                        return False
                    count+=1
            else:
                return False
            if count>1:
                return False
        return True