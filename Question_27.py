class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=0
        r=len(nums)-1

        if len(nums) == 0:
            return 0

        while l < r:
            if nums[l] == val:
                if nums[r] != val:
                    nums[l] = nums[r]
                    nums[r] = val 
                    l += 1
                r -= 1
            else:
                l += 1
        if nums[l] != val:     
            return l+1
        else: 
            if l>=r:
                return l
            return 0

        
