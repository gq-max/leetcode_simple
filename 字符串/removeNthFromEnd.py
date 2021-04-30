"""
删除链表的倒数第N个节点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

例如：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

输入：head = [1], n = 1
输出：[]

输入：head = [1,2], n = 1
输出：[1]

提示：
链表中结点的数目为 sz
"""
def removeNthFromEnd(head, n):
    """双指针"""
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
