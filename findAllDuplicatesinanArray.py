class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        Dict={}
        res=[]
        for i in nums:
            if Dict.get(i):
                res.append(i)
            else:
                Dict[i]=1
        return res