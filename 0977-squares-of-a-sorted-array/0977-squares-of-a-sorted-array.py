class Solution(object):
    def sortedSquares(self, nums):
        list = []
        for i in nums:
            a = i**2
            list.append(a)
        nums[:] = []
        nums = sorted(list)
        return nums
        
        
          