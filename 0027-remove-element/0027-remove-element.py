class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        temp_val = [ ]
        temp =  [ ]
        temp_num = [ ]
        a = "_"
        for i in nums:
            if i == val:
                temp_val.append(i)
                temp.append(a)
            else :
                temp_num.append(i)
        nums [:] = []
        nums.extend(temp_num)
                






        