"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium

Approach:
- Use sliding window with set
- Expand window and remove duplicates when needed

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        i=0
        result = 0

        for j in range(len(s)):
            if s[j] in visited:
                i= max(visited[s[j]], i)

            result = max(j-i+1, result)
            visited[s[j]] =  j+1

        return result  
