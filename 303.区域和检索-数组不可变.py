#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#


from typing import Optional,List
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # 初始化赋值
        self.preNsums = [0] * (len(nums) + 1)
        # 从第1项开始求和
        for i in range(1,len(self.preNsums)):
            self.preNsums[i] += self.preNsums[i-1] + self.nums[i-1]
    
    def sumRange1(self, left: int, right: int) -> int:
        return self.preNsums[right+1] - self.preNsums[left]
    
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left,right+1):
            sum+=self.nums[i]
        return sum
    
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

