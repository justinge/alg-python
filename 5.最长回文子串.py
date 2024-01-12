#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def getPalindrome(self, s:str,start1:int, start2:int)->list:
        while start1>=0 and start2 <len(s) and s[start1] == s[start2]:
            start1-=1
            start2+=1
        return s[start1+1:start2]
        
         
        
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            res1 = self.getPalindrome(s,i,i)
            res2 = self.getPalindrome(s,i,i+1)
            res = res1 if len(res1) > len(res) else res
            res = res2 if len(res2) > len(res) else res
        return res
       
# @lc code=end

# s = "babad"
# Solution().longestPalindrome(s)