"""
回文链表
请判断一个链表是否为回文链表。

例如：
输入: 1->2
输出: false

输入: 1->2->2->1
输出: true
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    """借助于栈（列表）"""
    l = head
    val_list = []
    while l:
        val_list.append(l.val)
        l = l.next
    if val_list[:] == val_list[::-1]:
        return True
    return False


def isPalindrome1(head):
    """双指针（快慢指针） + 列表反转"""
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    if fast:
        slow = slow.next
    slow = reverse_list(slow)
    fast = head
    while slow:
        if fast.val != slow.val:
            return False
        fast = fast.next
        slow = slow.next
    return True


def reverse_list(cur_node):
    pre_node = None
    while cur_node:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node
    return pre_node
