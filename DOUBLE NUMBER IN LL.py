class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convert_to_int(head):
    num = 0
    current = head
    while current:
        num = num * 10 + current.val
        current = current.next
    return num

def convert_to_linked_list(num):
    head = ListNode()
    current = head
    for digit in str(num):
        current.next = ListNode(int(digit))
        current = current.next
    return head.next

def double_linked_list(head):
    num = convert_to_int(head)
    doubled_num = num * 2
    return convert_to_linked_list(doubled_num)

head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(9)
doubled_list = double_linked_list(head)
while doubled_list:
    print(doubled_list.val)
    doubled_list = doubled_list.next
