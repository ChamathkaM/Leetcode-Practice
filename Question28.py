class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=0
        r=len(needle)

        while r <= len(haystack):
            haystacksub=haystack[l:r]
            if haystacksub == needle:
                return l
            l+=1
            r+=1
        return -1


        
