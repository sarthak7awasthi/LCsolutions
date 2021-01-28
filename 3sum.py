class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range(0,len(nums)-2):
            start=i+1
            end=len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while end>start:
                if nums[i]+nums[start]+nums[end]==0:
                    arr.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                elif nums[i]+nums[start]+nums[end]>0:
                    end-=1
                else:
                    start+=1
        testArr=[]
        for i in arr:
            if i in testArr:
                continue
            else:
                testArr.append(i)
        return testArr