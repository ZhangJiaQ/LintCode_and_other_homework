链表倒数第n个节点
样例
给出链表 3->2->1->5->null和n = 2，返回倒数第二个节点的值1.


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        #创建两个指针，一个指向表头，一个指向第N个元素
        if not head:
            return 0
        
        count = head
        i = 1
        while count.next:
            count = count.next
            i += 1
        while i-n>0:
            head = head.next
            i -= 1
        return head