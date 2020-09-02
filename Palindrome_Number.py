class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        if x==0 or x<10:
            return True
        if (x%10)==0:
            return False
        c=x
        n=0
        while x!=0:
            n=n*10+ x%10
            x=x//10
        
        if n ==c:
            return True
