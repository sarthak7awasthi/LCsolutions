class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        arr=[]
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                start=j+1
                end=len(nums)-1
                while start<end:
                    
                    if nums[i]+nums[j]+nums[start]+nums[end]==target:
                        arr.append([nums[i],nums[j],nums[start],nums[end]])
                        start+=1
                        end-=1
                    elif nums[i]+nums[j]+nums[start]+nums[end]>target:
                        end-=1
                    else:
                        start+=1
        newarr=[]
        for i in arr:
            if i not in newarr:
                newarr.append(i)
        return newarr