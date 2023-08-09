# Problema: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Pivote de tamaño y para llevar el string mas largo
        leght: int = 0
        p: str = ''
        for i in s: # iteramos sobre el string
            # Si hay una letra repetida, inicializamos la cadena quitando la que se repite
            # anviaj -> (anvi -> nvia)
            if i in p: p = f"{p[p.index(i)+1:]}" 
            p += i # Construimos la cadena mas larga
            leght = max(len(p), leght) # Actualizamos la cadena mas larga
        return leght

class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = Solution()
        test_cases = {
            "case1": (" ", 1),
            "case2": ("aa", 1),
            "case3": ("akfmo", 5),
            "case4": ("abdabd", 3),
            "case5": ("dvdf", 3),
            "case6": ("anviaj", 5),
            "case7": ("nfpdmpi", 5)
        }
        
        for name, (input_str, expected_output) in test_cases.items():
            with self.subTest(name=name):
                self.assertEqual(s.lengthOfLongestSubstring(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()

    algo = Solution()
    algo.lengthOfLongestSubstring("anviaj")
