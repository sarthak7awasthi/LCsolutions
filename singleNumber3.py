class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        Dict={}
        for i in nums:
            if Dict.get(i):
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
        arr=[]
        for key in Dict:
            if Dict[key]==1:
                arr.append(key)
        return arr