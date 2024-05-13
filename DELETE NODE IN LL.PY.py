class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(head, node_val):
    # Check if head node itself is the one to be deleted
    if head.val == node_val:
        return head.next

    prev = None
    current = head

    while current:
        if current.val == node_val:
            prev.next = current.next
            break
        prev = current
        current = current.next

    return head


# Example usage:
# Create the linked list
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

node_val = 5
new_head = deleteNode(head, node_val)

# Print the modified linked list
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
