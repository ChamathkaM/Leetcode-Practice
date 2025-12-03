class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        j = len(nums)-1
        while j >= 0:
            for i in range(len(nums)):
                if nums[i] == nums[j]:
                    if abs(i-j) <= k:
                        return True
            j =-1
        return False
