class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # python functionality
        # nums = nums[-k:] + nums[0:len(nums)-k]
        for i in range(k):
            temp=nums.pop()
            nums.insert(0,temp)
