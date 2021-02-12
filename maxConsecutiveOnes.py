class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        res=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                res.append(count)
                count=0
            if i==len(nums)-1:
                res.append(count)
        return max(res)
        