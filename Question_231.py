class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #optimized solution
        if n == 1:
            return True
        if n <=0:
            return False
        while n > 1:
            if n%2 ==0:
                n = n/2
            else:
                return False

        return True
        
