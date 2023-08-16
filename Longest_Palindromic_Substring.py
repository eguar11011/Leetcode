# https://leetcode.com/problems/longest-palindromic-substring/description/
import unittest
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i,j):
            left:int = i
            right:int = j
            current_p:str = ""

            if left == right:
                current_p = s[i]
                # Limite inferior y superior.
                while (left > 0) & (right < len(s)-1) and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                    current_p = s[left] +current_p +s[right]
            else:
                while (left >= 0) & (right <= len(s)-1) and s[left] == s[right]:
                    current_p = s[left] +current_p + s[right]
                    left -= 1
                    right += 1

            return current_p 
        
        lp:str = ""
        for i in range(len(s)):
            even = expand(i,i)
            odd = expand(i,i+1)
            if len(even)>len(odd): lp =  lp if len(lp) >=len(even) else even
            else: lp =  lp if len(lp) >len(odd) else odd
            
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
    unittest.main()

    s = Solution()
    print(s.longestPalindrome("ac")) 


            