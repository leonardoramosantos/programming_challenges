# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode(0)
        result_loop = result
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            d1 = l1.val if l1 != None else 0
            d2 = l2.val if l2 != None else 0
            sum_of_numbers = d1 + d2 + carry
            carry = sum_of_numbers // 10

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

            newNode = ListNode(sum_of_numbers % 10)
            result_loop.next = newNode
            result_loop = newNode

        return result.next