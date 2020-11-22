class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1=[]
        stack2=[]
        for i in S:
            if i!="#":
                stack1.append(i)
            else:
                if len(stack1)==0:
                    continue
                else:
                    stack1.pop()
                   
                    
        for j in T:
            if j!="#":
                stack2.append(j)
            else:
                if len(stack2)==0:
                    continue
                else:
                    stack2.pop()
                   
     
        
        if stack1==stack2:
            return True
        else:
            return False
            