#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        if not (fast and fast.next):
            return None
        hasCycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        if not hasCycle:
            return None
        slow = head
        while slow!=fast:
            slow = slow.next 
            fast = fast.next
        return slow
        
# @lc code=end

