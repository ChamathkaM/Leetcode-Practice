class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        carry = 0
        val = 0
        res=""


        for i in range(max(len(a),len(b))):
            digitA = a[i] if i < len(a) else 0
            digitB = b[i] if i < len(b) else 0
            val = int(digitA) + int(digitB) + carry
            char = str(val % 2)
            res =char +res
            carry = val // 2
            
        if carry:
            res = "1"+ res
        return res


        

