class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Dict={}
        for i in range(len(nums2)):
            if Dict.get(nums2[i],None)!=None:
                continue
            else:
                Dict[nums2[i]]=i
        for i in range(len(nums1)):
            val=nums1[i]
            for j in range(Dict.get(nums1[i])+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    nums1[i]=nums2[j]
                    break
            if nums1[i]==val:
                nums1[i]=-1
        return nums1