class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """  
        num1ind = m-1
        num2ind = n-1
        num1len=(m+n)-1

        while num1len>=0 and num2ind>=0 and num1ind>=0:

            if nums2[num2ind] > nums1[num1ind]:
                nums1[num1len] = nums2[num2ind]
                num2ind -= 1
                num1len -= 1

            else:
                print(num1len,num1ind)
                nums1[num1len] = nums1[num1ind]
                num1len -= 1
        return nums1




        
