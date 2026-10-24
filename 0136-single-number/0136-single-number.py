class Solution(object):
    def singleNumber(self, nums):
        
        temp = []
        duplicates = []
        count = 0
        for num in nums:
            if num in temp:
                duplicates.append(num)
            else :
                temp.append(num)
        
        for num in temp :
            if num in duplicates:
                count += 1
            else :
                return num
