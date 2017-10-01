合并两个排序链表
将两个排序链表合并为一个新的排序链表
样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。

解题思路：依次从l1,l2表头获取节点，将小的添加到l3

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        #解题思路：依次从l1,l2表头获取节点，将小的添加到l3
        if l1 is None: return l2
        if l2 is None: return l1
        
        l3 = ListNode(-1)
        cur = l3
        
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next =l1
                l1 = l1.next
            cur = cur.next
          
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
                
        return l3.next
            