# Last updated: 6/9/2026, 3:26:20 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        
4
5        n = len(nums)
6        
7        expected_ans = n * (n+1)//2
8        actual_ans = sum(nums)
9        
10        return expected_ans - actual_ans