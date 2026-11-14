class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)
    
        while low < high:
            mid = (low + high ) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid] :
                low = mid + 1 
            else :
                high = mid 
        
        if nums > target:
            return low
        else :
            return high
            
            
        
        
        