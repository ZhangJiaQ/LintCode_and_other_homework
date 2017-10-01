删除排序链表中的重复元素 
样例
给出 1->1->2->null，返回 1->2->null
给出 1->1->2->3->3->null，返回 1->2->3->null

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        #两根指针，如果next等于head，将next解套，当next不存在时停止循环
        if not head:
            return None
        current = head
        next = head.next
        while next:
            if next.val == current.val:
                current.next = next.next
                next = next.next
            else:
                current = current.next
                if next
                    next = next.next
        return head