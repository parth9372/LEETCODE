#Input: head = [0,3,1,0,4,5,2,0]
#Output: [4,11]
#Explanation:
#The above figure represents the given linked list. The modified list contains
#- The sum of the nodes marked in green: 3 + 1 = 4.
#- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

class Solution(object):
    def mergeNodes(self, head):
        modify = head.next  # Start from the node after the initial 0
        next_sum = modify

        while next_sum:
            total = 0
            # Find the sum of all nodes until you encounter a 0.
            while next_sum.val != 0:
                total += next_sum.val
                next_sum = next_sum.next

            # Assign the sum to the current node's value.
            modify.val = total
            # Move next_sum to the first non-zero value of the next block.
            next_sum = next_sum.next
            # Move modify also to this node.
            modify.next = next_sum
            modify = modify.next

        return head.next  # Skip the initial 0 node

