class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        nums = str(num)
        count = 0
        for i in range (len(nums)-k+1):
            s = int(nums[i:i+k])
            if s!=0 and num % s == 0 :
                count += 1
        return count
