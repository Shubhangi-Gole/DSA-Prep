"""
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/
Difficulty: Medium

Approach:
- Expand around center for each index
- Check both odd and even length palindromes
- Track longest substring

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expanAroundCenter(s , left, right):

            substring =''
            max_length = 0
            while left >= 0 and right < len(s) and s[left] ==s[right]:
                if right - left + 1> max_length:
                    max_length = right - left +1
                    substring = s[left: right+1]
                left-=1
                right +=1
            return substring

        result=''
        for i in range(len(s)):
            odd = expanAroundCenter(s, i, i)
            even = expanAroundCenter(s, i, i+1)

            if len(odd)>len(result):
                result = odd
            if len(even)> len(result):
                result = even
        return result
