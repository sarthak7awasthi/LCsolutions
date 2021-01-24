class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        pointer=1
        for i in nums:
            if i<=0:
                continue
            if i==pointer:
                pointer+=1
        return pointer
        