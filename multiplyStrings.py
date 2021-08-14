class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        Dict={}
        for i in range(10):
            Dict[str(i)]=i
        n1=0
        c=0
        for i in num1[::-1]:
            n1=n1+Dict.get(i)*(10**c)
            c+=1
            
        n2=0
        c=0
        for i in num2[::-1]:
            n2=n2+Dict.get(i)*(10**c)
            c+=1
  
        return str(n1*n2)
        
