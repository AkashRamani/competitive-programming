#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        answer = ['0' for i in range(n+1)]

        carry = 0

        i = len(num1)-1
        j = len(num2)-1
        while i >=0 or j >= 0: 
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            summ = n1+n2+ carry
            carry  = summ // 10
            
            val = summ % 10
            answer[n] = str(val)

            j-=1
            i-=1
            n-=1

        if carry:
            answer[0] = str(carry)

        # remove leading zeros
        index = 0
        for i, val in enumerate(answer):
            if val == "0" and i < len(answer)-1:
                index+=1
            else:
                break

        return ''.join(answer[index:])
# @lc code=end

