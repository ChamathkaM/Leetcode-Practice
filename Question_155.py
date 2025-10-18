class MinStack(object):

    def __init__(self):
        self.items=[]  

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.append(val)


    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()

        

    def top(self):
        """
        :rtype: int
        """
        if not self.items:
            return -1
        else:
            return self.items[-1]

        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.items:
            return -1
        # else:
        #     return self.items[-1]
        minval=self.items[0]
        for i in self.items:
            minval=min(i,minval)
        return minval
