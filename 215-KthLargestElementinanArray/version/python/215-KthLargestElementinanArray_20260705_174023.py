# Last updated: 7/5/2026, 5:40:23 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3
4
5        nums.sort(reverse=True)
6
7        return nums[k-1]
8        