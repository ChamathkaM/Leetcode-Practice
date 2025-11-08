class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = {}
        
        for val in nums:
            if val in set1:
                set1[val] += 1
            else:
                set1[val] = 1
        
        for i in set1:
            if set1[i] == 1:
                return i
        
