# https://leetcode.com/problems/zigzag-conversion/submissions/
import numpy as np
import math as m
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Cantidad de columnas posibles
        # Realizamos una regla de 3
        if len(s) == 1  or numRows == 1 : return s
        colunms_c: int = numRows-1
        num_c: int = numRows+numRows-2
        x: int =m.ceil(((colunms_c)* len(s))/num_c)
        # Matriz para rellenar
        matrix: np.array = np.empty((numRows, x), dtype=object)
        # [Fila, Columna]
        sr: int = 0 
        sc: int = 0
        switch: bool = True
        total_string: int = len(s)
        for c in s: 

            # Rellenar en vertical
            if switch:
                matrix[sr,sc] = c
                sr += 1
                if sr == numRows and sr-2 != 0: switch = False; sc +=1; sr -=2
                if sr-numRows == 0: sr=0; sc+=1
            # Rellenar en diagonal
            else:
                matrix[sr,sc] = c
                sc +=1
                sr -= 1
                if sr == 0: switch = True
            total_string -=1
            if total_string == 0: break    
        cadenas_por_fila = [''.join(str(caracter) for caracter in fila if caracter is not None) for fila in matrix]
        resultado = ''.join(cadenas_por_fila)
                
        return resultado
            
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
        