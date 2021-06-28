class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right= len(nums)-1
        result = -1
 
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                result = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        Res=[result]
        left = 0
        right= len(nums)-1
        result = -1
 
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                result = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        Res.append(result)
        return Res
        
