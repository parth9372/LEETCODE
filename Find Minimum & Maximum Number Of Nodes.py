#Input: head = [3,1]
#Output: [-1,-1]
#Explanation: There are no critical points in [3,1].

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        pre = head
        cur = head.next
        ans = [-1, -1]
        prePosition, curPosition, firstPosition, position = -1, -1, -1, 0

        while cur.next is not None:
            if (cur.val < pre.val and cur.val < cur.next.val) or (cur.val > pre.val and cur.val > cur.next.val):
                # local
                prePosition = curPosition
                curPosition = position

                if firstPosition == -1:
                    firstPosition = position
                if prePosition != -1:
                    if ans[0] == -1:
                        ans[0] = curPosition - prePosition
                    else:
                        ans[0] = min(ans[0], curPosition - prePosition)
                    ans[1] = position - firstPosition

            position += 1
            pre = cur
            cur = cur.next
        return ans