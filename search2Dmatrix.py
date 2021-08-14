class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target<=i[-1]:
                left =0
                right=len(i)-1
                
                while left<=right:
                    mid=(left+right)//2
                    if i[mid]==target:
                        return True
                    if i[mid]>target:
                        right=mid-1
                    else:
                        left=mid+1
                        
            else:
                continue
        return False
