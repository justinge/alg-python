#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from typing import Optional,List
import heapq
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        # 这里不可以写成 p = dummy.next, 此时p为None， 后面p的变化不会和dummy有关
        p = dummy
        pq = []
        for head in lists:
            if head:
              heapq.heappush(pq,(head.val,id(head),head))
              
        
        while pq:
            head = heapq.heappop(pq)[2]
            p.next = head
            p = p.next
            
            if head.next:
               heapq.heappush(pq,(head.next.val,id(head.next),head.next))
               
        return dummy.next  
                  
# @lc code=end


l = [[1,4,5],[1,3,4],[2,6]]
n1 = ListNode(1)
n4 = ListNode(4)
n5 = ListNode(5)
n4.next = n5 
n1.next = n4
h1 = n1

n1 = ListNode(1)
n3 = ListNode(3)
n4 = ListNode(4)
n3.next = n4 
n1.next = n3
h2 = n1

n2 = ListNode(2)
n6 = ListNode(6)
n2.next = n6 
h3 = n2


Solution().mergeKLists([h1,h2,h3])

