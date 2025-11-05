class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = len(nums) // 2
        ct = {}

        for i in nums: 
            if i in ct:
                ct[i] += 1
            else:
                ct[i] = 1
            print(i,ct[i])

            if ct[i] > maj:
                return i

        
