class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNodes(head, nodes_to_remove):
    if not head:
        return None

    # Create a dummy node to handle cases where head needs to be removed
    dummy = ListNode(-1)
    dummy.next = head

    prev = dummy
    current = head

    while current:
        if current.val in nodes_to_remove:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return dummy.next


# Example usage:
# Create the linked list
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

nodes_to_remove = {5, 2, 3}
new_head = removeNodes(head, nodes_to_remove)

# Print the modified linked list
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
