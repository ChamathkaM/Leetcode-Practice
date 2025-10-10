class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strout=""
        left=strs[0]
        for i in range(1,len(strs)):  
            right = strs[i]
            index = 0
            commonstr=""
            minlength = min(len(right),len(left))
            while index < minlength:               
                if left[index] == right[index]:
                    commonstr += left[index]                  
                    index += 1
                else:
                    break
            left = commonstr
        return left
                



    

        
