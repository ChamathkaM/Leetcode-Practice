class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s1=[]
        for i in range(len(s)):
            if s[i].isalnum():
                s1.append(lower(s[i]))
        
        print(s1)
        l = 0
        r = len(s1)-1

        while l < r:
            print(s1[l],s1[r])
            print(s1[l],s1[r])
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True

        
