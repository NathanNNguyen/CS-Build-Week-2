# Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

# For example, if we have the following linked list:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

# The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

# After the function executes, the state of the linked list should be:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def remove_kth_from_end(head, k):
    count = 1
    node = head
    while node:
        node = node.next
        count += 1

    tracer = 1
    cur = head
    prev = None
    while cur:
        prev = cur
        cur = prev.next
        tracer += 1
        if tracer == count - k and cur != None:
            # delete this node
            cur = cur.next
            prev.next = cur

    return head
