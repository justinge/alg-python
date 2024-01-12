#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
from typing import Optional,List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1,dummy2 = ListNode(-1),ListNode(-1)
        p,q = dummy1, dummy2
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            temp = head.next
            head.next = None
            head = temp
        p.next = dummy2.next
        return dummy1.next
# @lc code=end

[1,4,3,2,5,2]
3
a0 = ListNode(1)
a1 = ListNode(4)
a2 = ListNode(3)
a3 = ListNode(2)
a4 = ListNode(5)
a5 = ListNode(2)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
Solution().partition(a0,3)