# Last updated: 6/9/2026, 5:46:23 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        
4        left, right = 0, len(nums)
5
6        while left < right:
7
8            mid  = (left + right) // 2
9
10            if nums[mid] < target:
11                left = mid + 1
12            
13            else:
14                right = mid
15        
16        return left