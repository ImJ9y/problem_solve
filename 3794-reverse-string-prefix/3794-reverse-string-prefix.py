class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k < 2:
            return s
        
        new_s = list(s)
        temp = list(s)

        temp = temp[0:k][::-1]
        for i in range(len(temp)):
            new_s[i] = temp[i]
        
        return "".join(new_s)