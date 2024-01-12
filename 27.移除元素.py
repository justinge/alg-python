#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast,slow = 0,0
        while fast < len(nums):
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
            fast +=1
        return slow

# @lc code=end
nums = [3,2,2,3]
val = 3
Solution().removeElement(nums,3)