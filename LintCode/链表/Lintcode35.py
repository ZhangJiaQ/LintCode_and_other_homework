翻转链表 
样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        temp = None
        while head:
            next = head.next
            head.next = temp
            temp = head
            head = next
        
        return temp
        