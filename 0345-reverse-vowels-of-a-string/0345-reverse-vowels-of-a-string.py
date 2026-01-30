class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a','e','i','o','u']
        L, R = 0, len(s)-1

        while L < R:
            if s[L].lower() in vowels:
                while s[R].lower() not in vowels:
                    R -= 1
    
                s[L], s[R] = s[R], s[L]
                R -= 1
            L += 1
        
        return "".join(s)
