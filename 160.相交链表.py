#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA,headB
        if not p:
            return None
        if not q:
            return None
        while p!=q:
            if p:
                p = p.next
            else:
                p = headB
            if q:
                q = q.next
            else:
                q = headA
        
        if not (p and q):
            return None
        return p    
        
# @lc code=end

