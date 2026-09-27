class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = -1 if s[:1] == '-' else 1
        if s[:1] in '+-': s = s[1:]
        n = 0
        for c in s:
            if not c.isdigit(): break
            n = n * 10 + int(c)
        return max(-2**31, min(2**31 - 1, sign * n))