class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = match = 0
        star = -1
        while i < len(s):
            if j < len(p) and p[j] in (s[i], '?'): i += 1; j += 1
            elif j < len(p) and p[j] == '*': star, match = j, i; j += 1
            elif star >= 0: match += 1; i = match; j = star + 1
            else: return False
        while j < len(p) and p[j] == '*': j += 1
        return j == len(p)