class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]
            print(curr,reachableIndex)
            if curr == reachableIndex:
                break
                
        return reachableIndex >= len(nums) - 1