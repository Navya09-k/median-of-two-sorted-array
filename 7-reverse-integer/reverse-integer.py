class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        n = int(str(abs(x))[::-1]) * s
        return n if -(1 << 31) <= n < (1 << 31) else 0