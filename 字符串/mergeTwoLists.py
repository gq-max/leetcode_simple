"""
合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

例如：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：l1 = [], l2 = []
输出：[]

输入：l1 = [], l2 = [0]
输出：[0]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    """双指针"""
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    s = ListNode()
    head = s
    while l1 and l2:
        if l1.val < l2.val:
            s.val = l1.val
            s.next = ListNode()
            s = s.next
            l1 = l1.next
        else:
            s.val = l2.val
            s.next = ListNode()
            s = s.next
            l2 = l2.next
    if l1:
        s.val = l1.val
        s.next = l1.next
    if l2:
        s.val = l2.val
        s.next = l2.next
    return head

def mergeTwoLists2(l1, l2):
    """递归"""
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next =  mergeTwoLists2(l1, l2.next)
        return l2
