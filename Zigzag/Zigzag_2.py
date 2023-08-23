# https://leetcode.com/problems/zigzag-conversion/submissions/


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 0: return ""

        words: list = [[] for i in range(numRows)]
        step: int = 0
        switch: bool = True
        for c in s:
            words[step].append(c)
            if step < numRows-1 and switch:step+= 1
            elif step == numRows-1: switch = False; step-=1
            elif step == 0: switch = True; step+=1
            elif switch == False: step-=1

        ans: str = ''.join(caracter for sublista in words for caracter in sublista)
        return ans

            
"""
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

P   A   H   N
A P L S I I G
Y   I   R

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""
if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", numRows = 3))
        