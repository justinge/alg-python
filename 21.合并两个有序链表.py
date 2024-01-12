#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(-1)
        m = dummy
        p,q = list1,list2 
        while p and q:
            if p.val < q.val:
                m.next = p
                p = p.next
            else:
                m.next = q
                q = q.next
            m = m.next
        if p:
            m.next = p
        if q:
            m.next = q
        return dummy.next

# @lc code=end
l1 = [1,2,4]
l2 = [1,3,4]


n1 = ListNode(1)
n2 = ListNode(2)
n4 = ListNode(4)
n1.next = n2
n2.next = n4


n11 = ListNode(1)
n33 = ListNode(3)
n44 = ListNode(4)
n11.next = n33
n33.next = n44

Solution().mergeTwoLists(n1,n11)