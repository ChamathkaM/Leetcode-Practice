class Solution(object):
    #a simple problem
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if x==x[::-1]:
            return True
        else:
            return False
