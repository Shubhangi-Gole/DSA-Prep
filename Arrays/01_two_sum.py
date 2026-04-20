"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach:
- Use a hashmap (dictionary) to store visited elements
- For each number, check if (target - number) exists in hashmap

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]

            hash_map[num] = i

        return []
