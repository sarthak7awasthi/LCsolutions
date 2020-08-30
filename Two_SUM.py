class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        a=0
        b=len(nums)//2
        left = nums[a]
        right= nums[b]
        
        sum=0
        
        while target:
            sum= left+right
            if sum==target:
             
