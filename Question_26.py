class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        ct=0
        for r in range(1,len(nums)):
            if nums[r] == nums[l]:
                if ct == 0:
                    l+=1
                ct+=1
            else:
                nums[l] =nums[r]
                ct=0
        return l+1
