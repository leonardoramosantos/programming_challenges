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

        print(getNumber(l1), getNumber(l2))
        return getList(getNumber(l1) + getNumber(l2))
        

def getNumber(l_node):
    l_shift = 0
    result = 0
    node = l_node

    while (l_node != None):
        result = result + (l_node.val * (10 ** l_shift))
        l_shift = l_shift + 1
        l_node = l_node.next

    return result

def getList(val):
    first_node = ListNode()

    curr_node = first_node

    curr_node.val = val % 10
    val //= 10
    while (val > 0):
        curr_node.next = ListNode()
        curr_node = curr_node.next
        curr_node.val = val % 10
        val //= 10

    return first_node