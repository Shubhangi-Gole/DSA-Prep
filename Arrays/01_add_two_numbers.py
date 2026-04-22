"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium

Approach:
- Traverse both linked lists
- Add digits with carry
- Create new linked list for result

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s= ListNode(0)
        ptr = s
        c = 0
        while(l1 or l2 or c):
            if (l1):
                c += l1.val
                l1 = l1.next
            if(l2):
                c += l2.val
                l2 = l2.next
            ptr.next = ListNode(c % 10)
            ptr = ptr.next

            c = c//10
        return s.next            
