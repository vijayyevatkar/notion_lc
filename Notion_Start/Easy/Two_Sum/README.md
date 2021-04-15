========
Problem:
========

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

=========
Solution:
=========
1. Brute Force:
    @ Two indices, loop through entire array
    @ O(n^2) time
    @ O(1) space
2. Two pointer approach:
    @ Prerequisite -> Sort (this is needed to know which pointer to move) + HashMap to store indices
    @ Left End p1, Right End p2, Check and Move
    @ O(nlogn) for sort + O(n) to loop pointers => O(nlogn) time 
    @ O(n) for Hashmap - Space