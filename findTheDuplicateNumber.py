class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Dict={}
        for i in nums:
            if Dict.get(i):
                return i
            Dict[i]=1
            