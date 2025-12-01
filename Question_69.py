class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
    
        if x == 0:
            return 0
        first, last = 1, x

        while first <= last:
            mid =  first +(last-first)/2

            if x / mid == mid:
                return mid
            elif x / mid < mid:
                last = mid -1 
            else:
                first = mid + 1
        return last
        
