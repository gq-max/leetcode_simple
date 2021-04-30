"""
反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

例如：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

输入：head = [1,2]
输出：[2,1]

输入：head = []
输出：[]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if head is None:
        return None
    if head.next is None:
        return head
    stack = []
    s = head
    while s.next:
        stack.append(s.val)
        s = s.next
    stack.append(s.val)
    n = len(stack)
    s = head
    for i in range(n):
        val = stack[-1]
        s.val = val
        s = s.next
        stack = stack[:-1]


def reverseList1(head):
    pre_node = None
    while head:
        next_node = head.next
        head.next = pre_node
        pre_node = head
        head = next_node
    return pre_node
