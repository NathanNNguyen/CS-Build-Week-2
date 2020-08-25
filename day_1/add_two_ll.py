# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):

# # Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None

# class Solution:
#   def addTwoNumbers(self, l1, l2, c = 0):
#     # Fill this in.

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print result.val,
#   result = result.next
# # 7 0 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def addTwoNumbers(self, l1, l2, c=0):
#         cur_1, cur_2 = l1, l2
#         r = []
#         tenth = 0
#         while cur_1 != None:
#             total = 0
#             if tenth:
#                 total += cur_1.val + cur_2.val + tenth
#             else:
#                 total += cur_1.val + cur_2.val
#             if total >= 10:
#                 total = str(total)
#                 single = total[-1]
#                 tenth = total[0]
#                 total = int(single)
#             if int(tenth):
#                 tenth = int(tenth)
#             cur_1, cur_2 = cur_1.next, cur_2.next
#             r.append(total)
#         l3, l3.next, l3.next.next = ListNode(
#             r[0]), ListNode(r[1]), ListNode(r[2])
#         return l3


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r1 = ''
        current = l1
        while current != None:
            r1 += str(current.val)
            current = current.next

        r2 = ''
        current = l2
        while current != None:
            r2 += str(current.val)
            current = current.next

        r1 = int(r1[::-1])
        r2 = int(r2[::-1])

        result = r1 + r2
        res = [int(x) for x in str(result)[::-1]]

        l3, l3.next, l3.next.next = ListNode(
            res[0]), ListNode(res[1]), ListNode(res[2])
        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next
# 7 0 8
