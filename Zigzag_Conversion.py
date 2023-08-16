import numpy as np
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Cantidad de columnas posibles
        columns: int = int(len(s) / numRows) + len(s) % numRows
        # Matriz para rellenar
        matrix: np.array = np.empty((numRows, 7), dtype=object)
        # [Fila, Columna]
        sr: int = 0 
        sc: int = 0
        switch: bool = True
        for c in s: 
            # Rellenar en vertical
            if switch:
                matrix[sr,sc] = c
                sr += 1
                if sr == numRows: switch = False; sc +=1; sr -=1
                
            # Rellenar en diagonal
            else:
                sr -=1
                matrix[sr,sc] = c
                sc +=1
                if sr == 0: switch = True; sc -=1
                
        return matrix
            
"""
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

P   A   H   N
A P L S I I G
Y   I   R
"""
if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", numRows = 3))
        