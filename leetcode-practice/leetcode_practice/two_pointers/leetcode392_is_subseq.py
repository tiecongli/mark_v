class Solution:
    def is_subseq(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == len(s)
