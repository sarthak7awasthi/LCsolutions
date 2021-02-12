class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        last=nums[-1]
        i=len(nums)-2
        while count!=3:
            try:
                if nums[i]!=last:
                    last=nums[i]
                    count+=1
                    if count==3:
                        return nums[i]
                i-=1
            except:
                return max(nums)
   