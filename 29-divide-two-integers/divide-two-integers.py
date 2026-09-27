class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b, q = abs(dividend), abs(divisor), 0
        while a >= b:
            x, n = b, 1
            while a >= x << 1: x, n = x << 1, n << 1
            a -= x; q += n
        q = -q if s < 0 else q
        return max(-(1 << 31), min((1 << 31) - 1, q))