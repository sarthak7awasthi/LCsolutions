class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i<=len(nums):
            try:
                if nums[i]==nums[i-1] or nums[i]==nums[i+1]:
                    nums.pop(i)
                else:
                    i+=1
            except:
                i+=1
                continue
        return len(nums)
