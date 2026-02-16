class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for c in s:
            if c.isalnum():
                new_s += c.lower()
        
        return new_s == new_s[::-1]
        
        # L, R = 0, len(s)-1

        # while L < R:
        #     while L < R and not s[L].isalnum():
        #         L += 1
        #     while R > L and not s[R].isalnum():
        #         R -= 1

        #     if s[L].lower() != s[R].lower():
        #         return False
            
        #     L += 1
        #     R -= 1
        
        # return True
            