class Solution(object):
    def containsDuplicate(self, nums):
        temp = set( )
        for num in nums :
            if num in temp :
                return True
            else:
                temp.add(num)
        return False
        