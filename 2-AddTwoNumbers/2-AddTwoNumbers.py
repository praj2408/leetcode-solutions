# Last updated: 2/22/2026, 10:30:28 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        dummy = ListNode(0)
10        current = dummy
11        carry = 0
12
13        while l1 or l2 or carry:
14            val1 = l1.val if l1 else 0
15            val2 = l2.val if l2 else 0
16
17            total = val1 + val2 + carry
18            carry = total // 10
19
20            current.next = ListNode(total % 10)
21            current = current.next
22
23            if l1:
24                l1 = l1.next
25            if l2:
26                l2 = l2.next
27
28        return dummy.next