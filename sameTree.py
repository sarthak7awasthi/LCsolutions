# Passes 59/60 test cases


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def result(self,p,q):
    
        if (p==None and q==None):
          
            return True
        elif p==None and q!=None:
 
            return False
        elif q==None and p!=None:
     
            return False
        else:
            if q.val!=p.val:
               
                return False
            else:
          
                return self.result(p.left,q.left)
    def Result(self,p,q):

        if p==None and q==None:
     
            return True
        elif p==None and q!=None:
       
            return False
        elif q==None and p!=None:
          
            return False
        else:
            if q.val!=p.val:
               
                return False
            else:
               
                return self.Result(p.right,q.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif q==None and p!=None:
            return False
        left=self.result(p.left,q.left)
        right=self.Result(p.right,q.right)
        print(left,right)
        if (p.val==q.val) and left and right:
            return True
        else:
            return False
