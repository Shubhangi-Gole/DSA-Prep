"""
Problem: Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/
Difficulty: Medium

Approach:
- Extract digits using modulo
- Build reversed number
- Handle overflow (32-bit signed integer range)

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = 1

        if x <0:
            sign = -1
            x = x* -1

        while x>0:
            rem = x%10
            sum = sum*10 + rem
            x = x//10

        if not -2**31 <sum <2**31:
            return 0

        return sum * sign            


        
