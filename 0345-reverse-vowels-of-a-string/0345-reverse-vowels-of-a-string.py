class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a','e','i','o','u']
        L, R = 0, len(s)-1

        while L < R:
            if s[L].lower() in vowels:
                if s[R].lower() in vowels:
                    s[L], s[R] = s[R], s[L]
                    L += 1
                    R -= 1
                else:
                    R -= 1
            else:
                L += 1
        
        return "".join(s)
