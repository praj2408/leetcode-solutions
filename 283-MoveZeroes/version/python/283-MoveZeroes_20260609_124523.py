# Last updated: 6/9/2026, 12:45:23 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        j = 0
8
9        for i in range(len(nums)):
10
11            if nums[i] != 0:
12                nums[j],nums[i] = nums[i], nums[j]
13                j += 1
14        
15        return nums
16
17        