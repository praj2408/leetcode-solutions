# Last updated: 6/9/2026, 4:08:26 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3
4
5        left, right = 0, len(nums)-1
6
7        while left <= right:
8
9            mid = (left+right) // 2
10
11            if nums[mid] == target:
12                return mid
13            elif nums[mid] < target:
14                left = mid+1
15            else:
16                right = mid-1
17        
18        return -1
19        