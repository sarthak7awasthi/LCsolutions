class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k=s.split(" ")
        if len(pattern)!=len(k):
            return False
        Dict1={}
        Dict2={}
        Dict3={}
        c=0
        for i,j in zip(pattern,k):
            
            if Dict1.get(i):
                Dict2[c]=i
            else:
                Dict1[i]=j
                Dict2[c]=i
            c+=1
            Dict3[j]=1
        if len(Dict1)!=len(Dict3):
            return False
        string=""
        c=0
        for i in Dict2:
            if c==0:
                string+=Dict1[Dict2[i]]
            else:
                string=string+" "+Dict1[Dict2[i]]
            c+=1
       
        if string==s:
            return True
        else:
            return False