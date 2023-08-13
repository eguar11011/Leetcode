import unittest
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp: str = ""
        if len(s) == 1 or len(s) == 0: return s
        if s.count(s[0]) == len(s): return s
    
        # Iteramos bajo la suposición de que s es el centro de un palindromo
        for indice in range(len(s)):
            c:int = 0
            current_p:str = ""
            c_2: int = 0

            for j in range(1, len(s[:indice])+2):
                if indice+j-c_2 > len(s)-1: break
                if s[indice-c-1] == s[indice+j-c_2] and indice-c-1>-1: # Caso impar
                    current_p = s[indice-c-1:indice+j-c_2+1]

                if s[indice-c] == s[indice+j-c_2]  and ( not(indice-c-1>-1) or not s[indice-c-1] == s[indice+j-c_2]) : 
                    current_p = s[indice-c] +current_p +s[indice+j-c_2]
                if len(current_p) == 0:
                    current_p = s[indice]
                    c_2 += 1
                c +=1
                lp = lp if len(current_p)< len(lp) else current_p 
        if lp == "" and len(s)>0: lp= s[0]     
        return lp 
            
class TestSolution(unittest.TestCase):
    """
    Esta clase define pruebas unitarias para el método lengthOfLongestSubstring
    de una clase Solution.
    """

    def test_lengthOfLongestSubstring(self):
        """
        Prueba el método lengthOfLongestSubstring en diferentes casos de prueba.
        """
        s = Solution()  # Crea una instancia de la clase Solution

        # Define casos de prueba con entradas y salidas esperadas
        test_cases = {
            "case1": ("babbad", "abba"),
            "case2": ("babad", "aba"),
            "case3": ("a", "a"),
            "case4": ("ccc", "ccc"),
            "caso6": ("", ""),
            "caso7": ("bab", "bab"),
            "caso8": ("ac", "a"),
            "caso9": ("bb", "bb"),
            "caso10": ("cbbd", "bb"),
            "caso11": ("aaaa", "aaaa"),
            "caso12": ("abcba", "abcba"),
            "caso13": ("aacabdkacaa","aca")
        }

        # Itera a través de los casos de prueba
        for name, (input_str, expected_output) in test_cases.items():
            with self.subTest(name=name):
                # Utiliza subTest para aislar las pruebas individuales
                # Ejecuta el método lengthOfLongestSubstring con la entrada actual
                result = s.longestPalindrome(input_str)
                # Compara el resultado real con el resultado esperado
                self.assertEqual(result, expected_output)


if __name__ == "__main__":
    #unittest.main()

    s = Solution()
    print(s.longestPalindrome('aacabdkacaa')) 


            