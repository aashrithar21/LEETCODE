class Solution(object):
   
    def moveZeroes(self, nums):
        
        temp_zeros = []
        temp_nonzeros = []
        for i in nums:
            if i == 0:
                temp_zeros.append(i)
            else:
                temp_nonzeros.append(i)
        #nums = temp_nonzeros + temp_zeros
        nums[:] = []
        nums.extend( temp_nonzeros + temp_zeros)


        