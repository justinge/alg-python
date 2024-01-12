#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
from typing import Optional
import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reserve(self,head:Optional[ListNode])->Optional[ListNode]:
        """
        递归翻转链表
        """
        if (not head) or (not head.next):
            return head
        last = self.reserve(head.next)
        head.next.next = head
        head.next = None
        return last
    def reserve1(self,head:Optional[ListNode])->Optional[ListNode]:
        """
        迭代翻转链表
        """
        pre,cur,nxt = None,head,head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt 
        return pre
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        
        """
        head1 = copy.deepcopy(head)
        # 递归翻转链表
        # res = self.reserve(head1)
        #
        
        res = self.reserve1(head1)
        while head and res:
            if head.val == res.val:
                head = head.next
                res = res.next
            else:
                return False
        return True
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        
        if not (head and head.next):
            # return True
            pass
        # step1 找中点
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #step2 奇数slow需要向前挪动一位
        if fast:
            slow = slow.next
        # step3 左右指针    
        left,right= head,self.reserve(slow)
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

        
# @lc code=end
# 1,1,2,1
n0 = ListNode(1)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(1)
n0.next = n1
n1.next = n2
n2.next = n3
Solution().isPalindrome(n0)