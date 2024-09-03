#nput: bills = [5,5,5,10,20]
#Output: true
#Explanation:
#From the first 3 customers, we collect three $5 bills in order.
#From the fourth customer, we collect a $10 bill and give back a $5.
#From the fifth customer, we give a $10 bill and a $5 bill.
#Since all customers got correct change, we output true.

class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False

        five_dollers = 0
        ten_dollers = 0

        for x in bills:
            if x == 5:
                five_dollers += 1
            elif x == 10:
                if five_dollers > 0:
                    five_dollers -= 1
                else:
                    return False
                ten_dollers += 1
            else:
                if five_dollers > 0 and ten_dollers > 0:
                    five_dollers -= 1
                    ten_dollers -= 1
                elif five_dollers > 2:
                    five_dollers -= 3
                else:
                    return False
            print(five_dollers, ten_dollers)
        return True
#Example
solution = Solution()
bills = [5,5,5,10,20]
print(solution.lemonadeChange(bills))