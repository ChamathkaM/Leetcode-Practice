class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """


        sumval=0
        iprev=''

        for i in s:
            if i=='I':
                sumval+=1
            elif i== 'V':
                sumval+=5
                if iprev == 'I':
                    sumval-=2
            elif i == 'X':
                sumval+=10
                if iprev == 'I':
                    sumval-=2
            elif i == 'L':
                sumval+=50
                if iprev == 'X':
                    sumval-=20
            elif i == 'C':
                sumval+=100
                if iprev == 'X':
                    sumval-=20
            elif i == 'D':
                sumval+=500
                if iprev == 'C':
                    sumval-=200
            elif i == 'M':
                sumval+=1000
                if iprev == 'C':
                    sumval-=200
            iprev=i
        return sumval




        
