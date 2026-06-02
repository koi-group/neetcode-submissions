class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            smas = sorted(list(s))
            tmas = sorted(list(t))
            if smas == tmas:
                return True
            else:
                return False
        else:
            return False