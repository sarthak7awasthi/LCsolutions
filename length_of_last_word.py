class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip(" ")
     
        c=0
        
        for i in reversed(s):
            if i!=" ":
                c+=1
            else:
                return c
        return c
