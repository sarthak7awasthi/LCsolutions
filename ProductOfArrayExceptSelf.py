class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=1
        count=0
        zeroSituation=False
        for i in nums:
            if i!=0:
                L*=i
                continue
            if i==0:
                count+=1
                zeroSituation=True
        if count>1:
            for i in range(len(nums)):
                nums[i]*=0
            return nums
        for i in range(len(nums)):
            if zeroSituation and (nums[i]!=0):
                nums[i]=0
            elif zeroSituation and (nums[i]==0):
                nums[i]=L
            else:
                nums[i]=L//nums[i]
            
        return nums
        
