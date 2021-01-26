class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        Dict={}
        for i in nums:
            if Dict.get(i):
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
        for key in Dict:
            if Dict[key]==1:
                return key