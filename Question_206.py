class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node= None 
        while head:
            prev=head.next
            head.next=node
            node=head
            head=prev
        return node
