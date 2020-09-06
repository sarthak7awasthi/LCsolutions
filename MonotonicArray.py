class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i=0
        a=0
        b=0
        while i<len(A)-1:
            if A[i]<=A[i+1]:
                a=a+1
            if A[i]>=A[i+1]:
                b=b+1
            i+=1
        if a==len(A)-1 or b==len(A)-1:
            return True
        else:
            return False
