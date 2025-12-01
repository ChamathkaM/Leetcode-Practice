#not a successful solution
# proper solution should be implemented with by considering mid point
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(2,x+1):
            if i*i == x:
                return i
            elif i*i < x:
                num = i 
            else:
                return num
