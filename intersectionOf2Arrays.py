class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Dict = dict.fromkeys(nums1, 1)
        intersection=[]
        for i in nums2:
            if Dict.get(i):
                del Dict[i]
                intersection.append(i)
                
        return intersection
